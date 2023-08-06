import yaml
import argparse
from pathlib import Path
from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader, DistributedSampler

from src.trainers.ibot_trainer import iBOTTrainer
from src.augmentations.ibot import iBOTDataAugmentation
from src.datasets.wrappers.ibot_wrapper import ImageFolderMask
from src.utils.loader import Loader
from src.utils.utils import fix_random_seeds, init_distributed_mode, cleanup

my_parser = argparse.ArgumentParser(
    description='Trains iBOT on a given dataset.')
my_parser.add_argument('--config_path',
                       type=str,
                       required=True,
                       help='Path to the config yaml for iBOT.')
args = my_parser.parse_args()

if __name__ == "__main__":
    # load config yaml
    args.config_path = Path(args.config_path)
    if not args.config_path.exists():
        raise ValueError(
            f'Unable to find config yaml file: {args.config_path}')
    config = yaml.load(open(args.config_path, "r"), Loader=Loader)

    # initialize distribution
    init_distributed_mode()
    # seed everything
    fix_random_seeds(config['seed'])

    # load the train dataset
    train_path = config['dataset']['train_path']
    transform = iBOTDataAugmentation(**config['dataset']['augmentations'])
    train_dataset = ImageFolderMask(
        train_path,
        enc_keys=config['decryption']['keys'],
        transform=transform,
        patch_size=config['model']['student']['patch_size'],
        **config['dataset']['MIM'])
    sampler = DistributedSampler(train_dataset, shuffle=True)
    train_dataset = DataLoader(train_dataset,
                               sampler=sampler,
                               batch_size=config['batch_size'],
                               **config['dataset']['loader'])

    # load the val dataset
    val_path = config['dataset']['val_path']
    val_transform = transforms.Compose([
        transforms.Resize(256, interpolation=3),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    val_dataset = datasets.ImageFolder(val_path, transform=val_transform)
    val_dataset = DataLoader(val_dataset,
                             batch_size=config['batch_size'],
                             **config['dataset']['val_loader'])

    # initialize the trainer
    trainer = iBOTTrainer(train_dataset, val_dataset, config, args.config_path)
    # train
    trainer.fit()

    # cleanup distributed training
    cleanup()

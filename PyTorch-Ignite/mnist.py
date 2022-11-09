# -*- coding: utf-8 -*-
# weibifan 2022-10-31
#  

'''  
更多内容：https://github.com/pytorch/ignite/tree/master/examples/mnist

命令行参数的使用：ArgumentParser
进度条的使用：tqdm

Python的装饰符@ =Java的注解（Annotation）  ---说白了就是回调函数，也称hook函数
案例：原函数fun1计算两个数之和，后来发现还需要在求和之后求绝对值。

先定义一个函数求绝对值。
def fun2(fn):   后有补充函数（装饰函数）---回调函数场景中，用于指明一个预定义好的事件。
  value=fn()   获得函数返回值
  value=|value|  额外处理
  log()   常用于插入日志、性能测试、事务处理等等。

@fun2    ---回调函数场景中，用于指明一个预定义好的事件。
def fun1():    先有fun1（被装饰函数），发现功能不足，进行装饰。 ---事件响应函数。
   Xxx

案例：在回调函数场景中，框架或系统先实现fun2指定事件，程序员实现fun1，完成事件响应。这种场景，先有fun2，后有fun1。

用法1：调用fun1，此时系统先调用fun2，执行fun2时调用fun1。
用法2：调用fun2，执行中调用fun1。

'''

from argparse import ArgumentParser

import torch
import torch.nn.functional as F
from torch import nn
from torch.optim import SGD
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import Compose, Normalize, ToTensor
from tqdm import tqdm

from ignite.engine import create_supervised_evaluator, create_supervised_trainer, Events
from ignite.metrics import Accuracy, Loss
from ignite.utils import setup_logger


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


def get_data_loaders(train_batch_size, val_batch_size):
    
    data_transform = Compose([ToTensor(), Normalize((0.1307,), (0.3081,))])

    train_loader = DataLoader(
        MNIST(download=True, root="../data", transform=data_transform, train=True), batch_size=train_batch_size, 
        shuffle=True
    )

    val_loader = DataLoader(
        MNIST(download=False, root="../data", transform=data_transform, train=False), batch_size=val_batch_size, 
        shuffle=False
    )
    return train_loader, val_loader


def run(train_batch_size, val_batch_size, epochs, lr, momentum, log_interval):
    # 第1步，获取数据指针
    train_loader, val_loader = get_data_loaders(train_batch_size, val_batch_size)
    # 第2步，生成前向模型对象
    model = Net()
    
    device = "cpu"

    if torch.cuda.is_available():
        device = "cuda"

    model.to(device)  # Move model before creating optimizer
    
    # 第3步，构建trainer，包括前向模型，优化器，损失函数，
    optimizer = SGD(model.parameters(), lr=lr, momentum=momentum)
    criterion = nn.NLLLoss()
    trainer = create_supervised_trainer(model, optimizer, criterion, device=device)
    trainer.logger = setup_logger("trainer")

    # 第4步，构建评估器，包括模型，评估指标
    val_metrics = {"accuracy": Accuracy(), "nll": Loss(criterion)}
    evaluator = create_supervised_evaluator(model, metrics=val_metrics, device=device)
    evaluator.logger = setup_logger("evaluator")

    # 第5步 构建进度条
    pbar = tqdm(initial=0, leave=False, total=len(train_loader), desc=f"ITERATION - loss: {0:.2f}")
    
    # 第6步，实现事件的响应的hook函数，4个事件。
    # 迭代结束事件
    @trainer.on(Events.ITERATION_COMPLETED(every=log_interval))
    def log_training_loss(engine):
        pbar.desc = f"ITERATION - loss: {engine.state.output:.2f}"
        pbar.update(log_interval)

    # 轮询结束事件
    @trainer.on(Events.EPOCH_COMPLETED)
    def log_training_results(engine):
        pbar.refresh()
        evaluator.run(train_loader)
        metrics = evaluator.state.metrics
        avg_accuracy = metrics["accuracy"]
        avg_nll = metrics["nll"]
        tqdm.write(
            f"Training Results - Epoch: {engine.state.epoch} Avg accuracy: {avg_accuracy:.2f} Avg loss: {avg_nll:.2f}"
        )

    # 轮询结束事件，顺序？
    @trainer.on(Events.EPOCH_COMPLETED)
    def log_validation_results(engine):
        evaluator.run(val_loader)
        metrics = evaluator.state.metrics
        avg_accuracy = metrics["accuracy"]
        avg_nll = metrics["nll"]
        tqdm.write(
            f"Validation Results - Epoch: {engine.state.epoch} Avg accuracy: {avg_accuracy:.2f} Avg loss: {avg_nll:.2f}"
        )

        pbar.n = pbar.last_print_n = 0

    @trainer.on(Events.EPOCH_COMPLETED | Events.COMPLETED)
    def log_time(engine):
        tqdm.write(f"{trainer.last_event_name.name} took { trainer.state.times[trainer.last_event_name.name]} seconds")

    trainer.run(train_loader, max_epochs=epochs)
    pbar.close()


if __name__ == "__main__":
    
    # ①构建对象
    parser = ArgumentParser()
    # ②配置参数
    parser.add_argument("--batch_size", type=int, default=64, help="input batch size for training (default: 64)")
    parser.add_argument(
        "--val_batch_size", type=int, default=1000, help="input batch size for validation (default: 1000)"
    )
    parser.add_argument("--epochs", type=int, default=10, help="number of epochs to train (default: 10)")
    parser.add_argument("--lr", type=float, default=0.01, help="learning rate (default: 0.01)")
    parser.add_argument("--momentum", type=float, default=0.5, help="SGD momentum (default: 0.5)")
    parser.add_argument(
        "--log_interval", type=int, default=10, help="how many batches to wait before logging training status"
    )
    # ③解析输入字符串
    args = parser.parse_args()
    # ④调用
    run(args.batch_size, args.val_batch_size, args.epochs, args.lr, args.momentum, args.log_interval)
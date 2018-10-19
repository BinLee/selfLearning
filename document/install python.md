## mac安装python2和python3

本身mac上安装了python2

```shell
MICHELLI-MB0:document michelli$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

如何继续安装python3，并且同时并存两个环境。

1、安装brew

```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2、安装python3

````
brew install python3
````

安装失败后会提示link失败，这个时候需要手工操作下

````shell
sudo mkdir /usr/local/Frameworks
brew link python3
````

3、安装pip3

某些情况下，pip3不会随着python3自动安装，这个时候需要手工安装pip3

```shell
brew postinstall python3
```

4、创建虚拟环境

```
$mkdir ~/python/python3
$cd ~/python/python3
$sudo pip3 install virtualenv
$virtualenv venv_py3
$. venv_py3/bin/activate.  #启动虚拟环境
$deactivate     #退出虚拟环境
```

5、禁止在虚拟环境外部使用pip （可选）

```
echo "export PIP_REQUIRE_VIRTUALENV=true" >> ~/.bash_profile   #最后一行添加
source ～/.bash_profile
```


# rpm_package_learn
learn how to package rpm software

## Env
- OpenEuler 22.03
## 本地解压RPM
```
rpm2cpio filename.rpm | cpio -div -D directory_name
```
## 打包
- 整个过程参考[文档](https://rpm-packaging-guide.github.io/)
- 在openEuler上打包
```dnf install gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools
```
- 检测已安装的命令 `rpm -ql rpmdevtools | grep bin`

- 建立相关的软件包层级
```
$ rpmdev-setuptree
$ tree ~/rpmbuild/
/home/user/rpmbuild/
|-- BUILD
|-- RPMS
|-- SOURCES
|-- SPECS
`-- SRPMS
````
- 分别以c 语言，python  shell 打印 hello world 作为例子
```
rpmdev-newspec bello
# 修改对应的cello.spec
# 源码包 
rpmbuild -bs cello.spec
# 二进制包
rpmbuild -bb cello.spec
```
- 本地安装生成的二进制包
```
sudo dnf install ./*.rpm
```

## More 
- https://src.fedoraproject.org/
- https://rpm-packaging-guide.github.io/

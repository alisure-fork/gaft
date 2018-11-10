# GAFT Installation Instruction

**Note:**

After the version 0.5.6, GAFT dose not install mpi4py implicitly when executing `pip install gaft`. If you want to run GAFT in MPI parallel environment, you can install mpi4py manually

## 1. Install MPI implementations ([MPICH](http://www.mpich.org/downloads/), [OpenMPI](https://www.open-mpi.org/software/ompi/v3.0/))

### Ubuntu

``` shell
sudo apt install mpich
```

### macOS

``` shell
brew install mpich
```

### Windows

Download the [Microsoft MPI (MS-MPI)](http://msdn.microsoft.com/en-us/library/bb524831%28v=vs.85%29.aspx)

### Other platforms

See more details in http://www.mpich.org/downloads/

## 2. Install mpi4py

```shell
pip install mpi4py
```

## 3. Install GAFT

### Via pip

``` shell
pip install gaft
```
### From source

``` shell
git clone git@github.com:PytLab/gaft.git

cd gaft

python setup.py install
```

## 4. Run test

``` shell
cd gaft

python setup.py test
```


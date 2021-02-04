# Test-T3

## test if condor works on T3 machine
To test condor on different machines, change the `BASEDIR` in `condor_sub.py`

also add `Requirements =  machine == "r510-0-6.privnet"`
to `jdl_template`.

simply do `python condor_sub.py 2 '/bin/sleep 10'`
to test if we can run condor on `r510-0-6.privnet`

## test writing files to `/store/user` from lpc or lxplus
### Recipe

```bash
SCRAM_ARCH=slc7_amd64_gcc700
export SCRAM_ARCH
cmsrel  CMSSW_10_6_19
cd  CMSSW_10_6_19/src
cmsenv
git clone git@github.com:yihui-lai/test_T3.git
cd test_T3/
scram b -j 10
cd
```
For a quick test, run
```
cmsRun condor-simple.py
```

To run crab with productions, edit the `outLFNDirBase` in `runcrab.py`. Then
```
voms-proxy-init -voms cms
python runcrab.py
./submit_crab.sh
```




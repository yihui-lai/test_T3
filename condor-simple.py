
import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.ParameterSet.Config as cms

options = VarParsing.VarParsing('analysis')

options.register(
    'max',
    10, # default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int,          # string, int, or float
    ""
)
options.parseArguments()

process = cms.Process("CopyJob")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#        "/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/57EFD72B-F015-7640-9C02-2A79FBD5AC14.root"
        "/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/5D241DFC-1763-7347-8981-97E9ABF840A6.root"
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.max)
)

process.out = cms.OutputModule("PoolOutputModule",
     fileName = cms.untracked.string("test_t3.root"),
     outputCommands = cms.untracked.vstring('drop *')
)
process.e = cms.EndPath(process.out)



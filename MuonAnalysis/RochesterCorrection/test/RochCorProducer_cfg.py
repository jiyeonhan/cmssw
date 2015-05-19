# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms

process = cms.Process("ROCHCORPRODUCER")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
    )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        "/store/mc/Summer12_DR53X/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/00004/FCD7719B-6115-E211-8505-20CF30561716.root"       
        )
)

#Database output service
#process.load("CondCore.DBCommon.CondDBCommon_cfi")
#///// output database (in this case local sqlite file)
#process.CondDBCommon.connect = 'sqlite_file:RochCorDBobject.db'


#process.PoolDBOutputService = cms.Service("PoolDBOutputService",
#    process.CondDBCommon,
#    timetype = cms.untracked.string('runnumber'),
#    toPut = cms.VPSet(cms.PSet(
#        record = cms.string('aKeyword'),
#        tag = cms.string('RochCorDBobject_test"')
#    ))
#)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",                                                     RochCorProducer = cms.PSet(
        initialSeed = cms.untracked.uint32(1),
        engineName = cms.untracked.string('TRandom3')
        )
                                                   
)

process.RochCorProducer = cms.EDProducer(
    'RochCorProducer',
    MuonLabel = cms.InputTag("muons"),
    RochCorProducer = cms.PSet(    initialSeed = cms.untracked.uint32(82),
                                   engineName = cms.untracked.string('TRandom3')
                                   )
    )

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

process.p = cms.Path(process.RochCorProducer)

process.e = cms.EndPath(process.out)

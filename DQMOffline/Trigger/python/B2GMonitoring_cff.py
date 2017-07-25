import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.topDiLeptonHLTEventDQM_cfi import topDiLeptonHLTOfflineDQM

b2gDileptonHLTOfflineDQM = topDiLeptonHLTOfflineDQM.clone()
b2gDileptonHLTOfflineDQM.setup.directory = cms.string('HLT/B2GHLTOffline/Dileptonic/CrossTriggers')
b2gDileptonHLTOfflineDQM.setup.triggerExtras.pathsELECMU = cms.vstring(['HLT_Mu37_Ele27_CaloIdL_MW_v','HLT_Mu27_Ele37_CaloIdL_MW_v'])
b2gDileptonHLTOfflineDQM.setup.triggerExtras.pathsDIMUON = cms.vstring([''])
b2gDileptonHLTOfflineDQM.setup.triggerExtras.pathsDIELEC = cms.vstring([''])
b2gDileptonHLTOfflineDQM.preselection.trigger.select = cms.vstring(['HLT_Mu37_Ele27_CaloIdL_MW_v','HLT_Mu27_Ele37_CaloIdL_MW_v'])

b2gDimuonHLTOfflineDQM = topDiLeptonHLTOfflineDQM.clone()
b2gDimuonHLTOfflineDQM.setup.directory = cms.string('HLT/B2GHLTOffline/Dileptonic/Dimuon')
b2gDimuonHLTOfflineDQM.setup.triggerExtras.pathsELECMU = cms.vstring([''])
b2gDimuonHLTOfflineDQM.setup.triggerExtras.pathsDIMUON = cms.vstring(['HLT_Mu37_TkMu27_v'])
b2gDimuonHLTOfflineDQM.setup.triggerExtras.pathsDIELEC = cms.vstring([''])
b2gDimuonHLTOfflineDQM.preselection.trigger.select = cms.vstring(['HLT_Mu37_TkMu27'])



b2gMonitorHLT = cms.Sequence(
    b2gDileptonHLTOfflineDQM*
    b2gDimuonHLTOfflineDQM

)

import FWCore.ParameterSet.Config as cms

b2gEfficiency_ElMu = cms.EDAnalyzer("DQMGenericClient",
    subDirs        = cms.untracked.vstring("HLT/B2GHLTOffline/Dileptonic/Dimuon/CrossTriggers"),
    verbose        = cms.untracked.uint32(0), # Set to 2 for all messages
                                      
    resolution     = cms.vstring(),
    efficiency     = cms.vstring(
        "effic_muPt_1       'efficiency vs leading muon pt; muon pt [GeV]; efficiency' muPt_1_numerator       muPt_1_denominator",
        "effic_muEta_1       'efficiency vs leading muon eta; muon eta ; efficiency' muEta_1_numerator       muEta_1_denominator",
        "effic_muPhi_1       'efficiency vs leading muon phi; muon phi ; efficiency' muPhi_1_numerator       muPhi_1_denominator",
        "effic_elePt_1       'efficiency vs electron pt; electron pt [GeV]; efficiency' elePt_1_numerator       elePt_1_denominator",
        "effic_eleEta_1       'efficiency vs electron eta; electron eta ; efficiency' eleEta_1_numerator       eleEta_1_denominator",
        "effic_elePhi_1       'efficiency vs electron phi; electron phi ; efficiency' elePhi_1_numerator       elePhi_1_denominator",
    ),
)

b2gEfficiency_diMu = cms.EDAnalyzer("DQMGenericClient",
    subDirs        = cms.untracked.vstring("HLT/B2GHLTOffline/Dileptonic/Dimuon/"),
    verbose        = cms.untracked.uint32(0), # Set to 2 for all messages
                                      
    resolution     = cms.vstring(),
    efficiency     = cms.vstring(
        "effic_muPt_1       'efficiency vs leading muon pt; muon pt [GeV]; efficiency' muPt_1_numerator       muPt_1_denominator",
        "effic_muEta_1       'efficiency vs leading muon eta; muon eta ; efficiency' muEta_1_numerator       muEta_1_denominator",
        "effic_muPhi_1       'efficiency vs leading muon phi; muon phi ; efficiency' muPhi_1_numerator       muPhi_1_denominator",
        "effic_muPt_2       'efficiency vs sub-leading muon pt; muon pt [GeV]; efficiency' muPt_2_numerator       muPt_2_denominator",
        "effic_muEta_2       'efficiency vs sub-leading muon eta; muon eta ; efficiency' muEta_2_numerator       muEta_2_denominator",
        "effic_muPhi_2       'efficiency vs sub-leading muon phi; muon phi ; efficiency' muPhi_2_numerator       muPhi_2_denominator",
    ),
)

b2gClient = cms.Sequence(
  b2gEfficiency_ElMu
  + b2gEfficiency_diMu
)

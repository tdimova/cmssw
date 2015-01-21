# getDatasets.py

import FWCore.ParameterSet.Config as cms


# dump of the Stream A Datasets defined in the HLT table as Stream A Datasets

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetInitialPD_selector
streamA_datasetInitialPD_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetInitialPD_selector.l1tResults = cms.InputTag('')
streamA_datasetInitialPD_selector.throw      = cms.bool(False)
streamA_datasetInitialPD_selector.triggerConditions = cms.vstring( ('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p3_v1', 
    'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1', 
    'HLT_AK8PFJet360TrimMod_Mass30_v1', 
    'HLT_BTagMu_DiJet110_Mu5_v1', 
    'HLT_BTagMu_DiJet20_Mu5_v1', 
    'HLT_BTagMu_DiJet40_Mu5_v1', 
    'HLT_BTagMu_DiJet70_Mu5_v1', 
    'HLT_BTagMu_Jet300_Mu5_v1', 
    'HLT_CaloJet500_NoJetID_v1', 
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_BTagCSV0p7_v1', 
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_v1', 
    'HLT_DiCentralPFJet70_PFMET120_NoiseCleaned_v1', 
    'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v1', 
    'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v1', 
    'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v1', 
    'HLT_DiPFJetAve100_HFJEC_v1', 
    'HLT_DiPFJetAve160_HFJEC_v1', 
    'HLT_DiPFJetAve220_HFJEC_v1', 
    'HLT_DiPFJetAve300_HFJEC_v1', 
    'HLT_DiPFJetAve30_HFJEC_v1', 
    'HLT_DiPFJetAve60_HFJEC_v1', 
    'HLT_DiPFJetAve80_HFJEC_v1', 
    'HLT_Dimuon0_Jpsi_Muon_v1', 
    'HLT_Dimuon0_Upsilon_Muon_v1', 
    'HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v1', 
    'HLT_Dimuon0er16_Jpsi_NoVertexing_v1', 
    'HLT_Dimuon13_PsiPrime_v1', 
    'HLT_Dimuon13_Upsilon_v1', 
    'HLT_Dimuon20_Jpsi_v1', 
    'HLT_Dimuon6_Jpsi_NoVertexing_v1', 
    'HLT_DoubleEle24_22_eta2p1_WP85_Gsf_v1', 
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v1', 
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1', 
    'HLT_DoubleEle8_CaloIdL_TrkIdVL_Mass8_PFHT300_v1', 
    'HLT_DoubleIsoMu17_eta2p1_v1', 
    'HLT_DoubleJet90_Double30_DoubleCSV0p5_v1', 
    'HLT_DoubleJet90_Double30_TripleCSV0p5_v1', 
    'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
    'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v1', 
    'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v1', 
    'HLT_DoubleMu33NoFiltersNoVtx_v1', 
    'HLT_DoubleMu38NoFiltersNoVtx_v1', 
    'HLT_DoubleMu4_3_Bs_v1', 
    'HLT_DoubleMu4_3_Jpsi_Displaced_v1', 
    'HLT_DoubleMu4_JpsiTrk_Displaced_v1', 
    'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v1', 
    'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v1', 
    'HLT_DoubleMu8_Mass8_PFHT300_v1', 
    'HLT_DoublePhoton85_v1', 
    'HLT_ECALHT800_v1', 
    'HLT_Ele105_CaloIdVT_GsfTrkIdT_v1', 
    'HLT_Ele10_CaloIdL_TrackIdVL_CentralPFJet30_BTagCSV0p5PF_v1', 
    'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
    'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Ele15_IsoVVVL_BTagtop8CSV07_PFHT400_v1', 
    'HLT_Ele15_IsoVVVL_PFHT400_PFMET70_v1', 
    'HLT_Ele15_IsoVVVL_PFHT600_v1', 
    'HLT_Ele15_PFHT300_v1', 
    'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v1', 
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1', 
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Ele18_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
    'HLT_Ele20WP60_Ele8_Mass55_v1', 
    'HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1', 
    'HLT_Ele22_eta2p1_WP85_Gsf_v1', 
    'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
    'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1', 
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Ele25WP60_SC4_Mass55_v1', 
    'HLT_Ele25_eta2p1_WP85_Gsf_PFMET80_boostedW_v1', 
    'HLT_Ele27_WP85_Gsf_v1', 
    'HLT_Ele27_eta2p1_WP85_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
    'HLT_Ele27_eta2p1_WP85_Gsf_HT200_v1', 
    'HLT_Ele27_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1', 
    'HLT_Ele32_eta2p1_WP85_Gsf_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
    'HLT_Ele32_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1', 
    'HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v1', 
    'HLT_Ele35_eta2p1_WP85_Gsf_v1', 
    'HLT_Ele40_eta2p1_WP85_Gsf_v1', 
    'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1', 
    'HLT_HT200_v1', 
    'HLT_HT250_v1', 
    'HLT_HT300_v1', 
    'HLT_HT350_DisplacedDijet80_DisplacedTrack_v1', 
    'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v1', 
    'HLT_HT350_v1', 
    'HLT_HT400_v1', 
    'HLT_HT650_DisplacedDijet80_Inclusive_v1', 
    'HLT_HT750_DisplacedDijet80_Inclusive_v1', 
    'HLT_IsoMu16_eta2p1_CaloMET30_LooseIsoPFTau50_Trk30_eta2p1_v1', 
    'HLT_IsoMu16_eta2p1_CaloMET30_v1', 
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v1', 
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1', 
    'HLT_IsoMu17_eta2p1_MediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
    'HLT_IsoMu17_eta2p1_v1', 
    'HLT_IsoMu20_eta2p1_v1', 
    'HLT_IsoMu24_eta2p1_LooseIsoPFTau20_v1', 
    'HLT_IsoMu24_eta2p1_v1', 
    'HLT_IsoMu27_v1', 
    'HLT_IsoTkMu20_eta2p1_v1', 
    'HLT_IsoTkMu24_eta2p1_v1', 
    'HLT_IsoTkMu27_v1', 
    'HLT_JetE30_NoBPTX3BX_NoHalo_v1', 
    'HLT_JetE30_NoBPTX_v1', 
    'HLT_JetE50_NoBPTX3BX_NoHalo_v1', 
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1', 
    'HLT_L1_TripleJet_VBF_v1', 
    'HLT_L2DoubleMu23_NoVertex_v1', 
    'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v1', 
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v1', 
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu10_NoVertex_NoBPTX_v1', 
    'HLT_L2Mu20_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu30_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v1', 
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_v1', 
    'HLT_MET75_IsoTrk50_v1', 
    'HLT_MET90_IsoTrk50_v1', 
    'HLT_MonoCentralPFJet140_PFMETNoMu100_PFMHTNoMu140_NoiseCleaned_v1', 
    'HLT_MonoCentralPFJet140_PFMETNoMu140_PFMHTNoMu140_NoiseCleaned_v1', 
    'HLT_MonoCentralPFJet150_PFMETNoMu150_PFMHTNoMu150_NoiseCleaned_v1', 
    'HLT_Mu10_CentralPFJet30_BTagCSV0p5PF_v1', 
    'HLT_Mu12_Photon25_CaloIdL_L1ISO_v1', 
    'HLT_Mu12_Photon25_CaloIdL_L1OR_v1', 
    'HLT_Mu12_Photon25_CaloIdL_v1', 
    'HLT_Mu14er_PFMET120_NoiseCleaned_v1', 
    'HLT_Mu15_IsoVVVL_BTagCSV07_PFHT400_v1', 
    'HLT_Mu15_IsoVVVL_PFHT400_PFMET70_v1', 
    'HLT_Mu15_IsoVVVL_PFHT600_v1', 
    'HLT_Mu15_PFHT300_v1', 
    'HLT_Mu16_eta2p1_CaloMET30_v1', 
    'HLT_Mu17_Mu8_DZ_v1', 
    'HLT_Mu17_Mu8_SameSign_DPhi_v1', 
    'HLT_Mu17_Mu8_SameSign_v1', 
    'HLT_Mu17_Photon30_CaloIdL_L1ISO_v1', 
    'HLT_Mu17_Photon35_CaloIdL_L1ISO_v1', 
    'HLT_Mu17_TkMu8_DZ_v1', 
    'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v1', 
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1', 
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v1', 
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1', 
    'HLT_Mu17_TrkIsoVVL_v1', 
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Mu24_TrkIsoVVL_v1', 
    'HLT_Mu24_eta2p1_v1', 
    'HLT_Mu25_TkMu0_dEta18_Onia_v1', 
    'HLT_Mu27_TkMu8_v1', 
    'HLT_Mu27_v1', 
    'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v1', 
    'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v1', 
    'HLT_Mu30_TkMu11_v1', 
    'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v1', 
    'HLT_Mu34_TrkIsoVVL_v1', 
    'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v1', 
    'HLT_Mu3er_PFHT140_PFMET125_NoiseCleaned_v1', 
    'HLT_Mu40_TkMu11_v1', 
    'HLT_Mu40_eta2p1_PFJet200_PFJet50_v1', 
    'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v1', 
    'HLT_Mu45_eta2p1_v1', 
    'HLT_Mu50_v1', 
    'HLT_Mu6_PFHT200_PFMET100_NoiseCleaned_BTagCSV07_v1', 
    'HLT_Mu6_PFHT200_PFMET125_NoiseCleaned_v1', 
    'HLT_Mu7p5_L2Mu2_Jpsi_v1', 
    'HLT_Mu7p5_L2Mu2_Upsilon_v1', 
    'HLT_Mu7p5_Track2_Jpsi_v1', 
    'HLT_Mu7p5_Track2_Upsilon_v1', 
    'HLT_Mu7p5_Track3p5_Jpsi_v1', 
    'HLT_Mu7p5_Track3p5_Upsilon_v1', 
    'HLT_Mu7p5_Track7_Jpsi_v1', 
    'HLT_Mu7p5_Track7_Upsilon_v1', 
    'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v1', 
    'HLT_Mu8_Ele8_CaloIdL_TrkIdVL_Mass8_PFHT300_v1', 
    'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v1', 
    'HLT_Mu8_TrkIsoVVL_v1', 
    'HLT_PFHT200_DiPFJet90_PFAlphaT0p57_v1', 
    'HLT_PFHT250_DiPFJet90_PFAlphaT0p55_v1', 
    'HLT_PFHT300_DiPFJet90_PFAlphaT0p53_v1', 
    'HLT_PFHT350_DiPFJet90_PFAlphaT0p52_v1', 
    'HLT_PFHT350_PFMET120_NoiseCleaned_v1', 
    'HLT_PFHT350_v1', 
    'HLT_PFHT400_DiPFJet90_PFAlphaT0p51_v1', 
    'HLT_PFHT550_4Jet_v1', 
    'HLT_PFHT600_v1', 
    'HLT_PFHT650_4Jet_v1', 
    'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v1', 
    'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v1', 
    'HLT_PFHT650_v1', 
    'HLT_PFHT750_4Jet_v1', 
    'HLT_PFHT900_v1', 
    'HLT_PFJet140_v1', 
    'HLT_PFJet200_v1', 
    'HLT_PFJet260_v1', 
    'HLT_PFJet320_v1', 
    'HLT_PFJet400_v1', 
    'HLT_PFJet40_v1', 
    'HLT_PFJet450_v1', 
    'HLT_PFJet500_v1', 
    'HLT_PFJet60_v1', 
    'HLT_PFJet80_v1', 
    'HLT_PFMET120_NoiseCleaned_BTagCSV07_v1', 
    'HLT_PFMET120_NoiseCleaned_Mu5_v1', 
    'HLT_PFMET120_PFMHT120_IDLoose_v1', 
    'HLT_PFMET170_NoiseCleaned_v1', 
    'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon120_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon120_v1', 
    'HLT_Photon135_PFMET100_NoiseCleaned_v1', 
    'HLT_Photon135_PFMET40_v1', 
    'HLT_Photon155_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon165_HE10_v1', 
    'HLT_Photon175_v1', 
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon22_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon22_v1', 
    'HLT_Photon250_NoHE_v1', 
    'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v1', 
    'HLT_Photon28_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon14_AND_HE10_R9Id65_Mass50_Eta1p5_v1', 
    'HLT_Photon300_NoHE_v1', 
    'HLT_Photon30_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon30_v1', 
    'HLT_Photon36_R9Id85_AND_CaloId24b40e_Iso50T80L_Photon18_AND_HE10_R9Id65_Mass30_v1', 
    'HLT_Photon36_R9Id85_AND_CaloId24b40e_Iso50T80L_Photon18_AND_HE10_R9Id65_v1', 
    'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon18_AND_HE10_R9Id65_Mass70_v1', 
    'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v1', 
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon36_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon36_v1', 
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon50_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon50_v1', 
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon75_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon75_v1', 
    'HLT_Photon90_CaloIdL_PFHT500_v1', 
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon90_R9Id90_HE10_Iso40_v1', 
    'HLT_Photon90_v1', 
    'HLT_Physics_v1', 
    'HLT_QuadJet45_DoubleCSV0p5_v1', 
    'HLT_QuadJet45_TripleCSV0p5_v1', 
    'HLT_QuadMuon0_Dimuon0_Jpsi_v1', 
    'HLT_QuadMuon0_Dimuon0_Upsilon_v1', 
    'HLT_QuadPFJet_BTagCSV_VBF_v1', 
    'HLT_QuadPFJet_VBF_v1', 
    'HLT_Rsq0p36_v1', 
    'HLT_RsqMR260_Rsq0p09_MR200_4jet_v1', 
    'HLT_RsqMR260_Rsq0p09_MR200_v1', 
    'HLT_RsqMR300_Rsq0p09_MR200_4jet_v1', 
    'HLT_RsqMR300_Rsq0p09_MR200_v1', 
    'HLT_TkMu24_eta2p1_v1', 
    'HLT_TkMu27_v1', 
    'HLT_TripleMu_12_10_5_v1', 
    'HLT_ZeroBias_v1' ) )

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetTemplates_selector
streamA_datasetTemplates_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetTemplates_selector.l1tResults = cms.InputTag('')
streamA_datasetTemplates_selector.throw      = cms.bool(False)
streamA_datasetTemplates_selector.triggerConditions = cms.vstring('HLT_IsoMu24_v1', 
    'HLT_IsoTkMu24_v1', 
    'HLT_ReducedIterativeTracking_v1')


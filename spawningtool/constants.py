"""
spawningtool.constants
~~~~~~~~~~~~~~~~~~~~~~
"""

BO_EXCLUDED = set([
    'MULE',
    'ReaperPlaceholder',
    'Interceptor'
    'AutoTurret',
    'PointDefenseDrone',
    'Locust',
    'LocustMP',
    'LocustMPFlyer',  # LotV Alpha Mod
    'Changeling',
    'InfestedTerran',
    'Overseer',
    'Broodling',
    'BroodlingEscort',  # the guys that fly with the Brood Lord
    'Larva',
    'CreepTumor',
    'CreepTumorQueen',
    'InfestedTerransEgg',
    'AutoTurret',
    'InfestedTerran',
    'Interceptor',
    'SwarmHostBurrowed',
    'InvisibleTargetDummy',  # LotV alpha mod
    'InterceptorFree',  # LotV alpha mod
    'AdeptPhaseShift',
])

BO_CHANGED_EXCLUDED = set([
    'VikingAssault',  # various viking transforms
    'VikingFighter',
    'Viking',
    'WidowMine',  # burrowing
    'Zergling',  # generated when Banelings spawn
])

BUILD_TIMES = {
    # terran units
    'SCV': 17,
    'Marine': 25,
    'Marauder': 30,
    'Reaper': 40,
    'Ghost': 40,
    'BattleHellion': 30,  # Hellbat
    'Hellion': 30,
    'Hellbat': 30,
    'WidowMine': 40,
    'SiegeTank': 45,
    'Thor': 60,
    'Viking': 42,
    'VikingFighter': 42,  # all born as VikingFighters, but others in here for coverage
    'VikingAssault': 42,
    'Medivac': 42,
    'Raven': 60,
    'Banshee': 60,
    'Battlecruiser': 90,
    # protoss units
    'Probe': 17,
    'Zealot': 38,
    'Stalker': 42,
    'Sentry': 37,
    'MothershipCore': 30,
    'HighTemplar': 55,
    'DarkTemplar': 55,
    'Immortal': 55,
    'Colossus': 75,
    'Archon': 12,
    'Observer': 30,
    'WarpPrism': 50,
    'Phoenix': 35,
    'VoidRay': 60,
    'Oracle': 50,
    'Tempest': 60,
    'Carrier': 90,  # 120 in HotS
    # zerg units
    'Drone': 17,
    'Queen': 50,
    'Zergling': 24,
    'Baneling': 20,
    'Roach': 27,
    'Hydralisk': 33,
    'SwarmHost': 40,
    'Infestor': 50,
    'Ultralisk': 55,
    'NydusWorm': 20,
    'NydusCanal': 20,
    'Overlord': 25,
    'Mutalisk': 33,
    'Corruptor': 40,
    'BroodLord': 34,
    'Viper': 40,
    # zerg upgrades
    'ZergMeleeWeaponsLevel1': 160,
    'ZergMeleeWeaponsLevel2': 190,
    'ZergMeleeWeaponsLevel3': 220,
    'ZergMissileWeaponsLevel1': 160,
    'ZergMissileWeaponsLevel2': 190,
    'ZergMissileWeaponsLevel3': 220,
    'ZergGroundArmorsLevel1': 160,
    'ZergGroundArmorsLevel2': 190,
    'ZergGroundArmorsLevel3': 220,
    'ZergFlyerWeaponsLevel1': 160,
    'ZergFlyerWeaponsLevel2': 190,
    'ZergFlyerWeaponsLevel3': 220,
    'ZergFlyerArmorsLevel1': 160,
    'ZergFlyerArmorsLevel2': 190,
    'ZergFlyerArmorsLevel3': 220,
    'zerglingmovementspeed': 110,
    'zerglingattackspeed': 130,
    'CentrificalHooks': 110,
    'GlialReconstitution': 110,
    'TunnelingClaws': 110,
    'hydraliskspeed': 80,  # Grooved Spines
    'HydraliskSpeedUpgrade': 100,  # Muscular Augments
    'overlordspeed': 60,
    'overlordtransport': 130,
    'Burrow': 100,
    'InfestorEnergyUpgrade': 80,
    'ChitinousPlating': 110,
    'LocustLifetimeIncrease': 120,
    # terran upgrades
    'TerranInfantryWeaponsLevel1': 160,
    'TerranInfantryWeaponsLevel2': 190,
    'TerranInfantryWeaponsLevel3': 220,
    'TerranInfantryArmorsLevel1': 160,
    'TerranInfantryArmorsLevel2': 190,
    'TerranInfantryArmorsLevel3': 220,
    'TerranVehicleWeaponsLevel1': 160,
    'TerranVehicleWeaponsLevel2': 190,
    'TerranVehicleWeaponsLevel3': 220,
    'TerranVehicleArmorsLevel1': 160,
    'TerranVehicleArmorsLevel2': 190,
    'TerranVehicleArmorsLevel3': 220,
    'TerranShipWeaponsLevel1': 160,
    'TerranShipWeaponsLevel2': 190,
    'TerranShipWeaponsLevel3': 220,
    'TerranShipArmorsLevel1': 160,
    'TerranShipArmorsLevel2': 190,
    'TerranShipArmorsLevel3': 220,
    'TerranVehicleAndShipWeaponsLevel1': 160,
    'TerranVehicleAndShipWeaponsLevel2': 190,
    'TerranVehicleAndShipWeaponsLevel3': 220,
    'TerranVehicleAndShipArmorsLevel1': 160,
    'TerranVehicleAndShipArmorsLevel2': 190,
    'TerranVehicleAndShipArmorsLevel3': 220,
    'HighCapacityBarrels': 110,
    'Stimpack': 170,
    'PunisherGrenades': 60,
    'ShieldWall': 110,  # ? Combat Shield?
    'MedivacCaduceusReactor': 80,
    'PersonalCloaking': 120,
    'GhostMoebiusReactor': 80,
    'NeosteelFrame': 110,
    'HiSecAutoTracking': 80,
    'TerranBuildingArmor': 140,
    'BansheeCloak': 110,
    'DurableMaterials': 110,
    'RavenCorvidReactor': 110,
    'StrikeCannons': 110,
    'DrillClaws': 110,
    'TransformationServos': 110,
    'BattlecruiserBehemothReactor': 80,
    'BattlecruiserEnableSpecializations': 60,
    # protoss upgrades
    'ProtossGroundWeaponsLevel1': 160,
    'ProtossGroundWeaponsLevel2': 190,
    'ProtossGroundWeaponsLevel3': 220,
    'ProtossGroundArmorsLevel1': 160,
    'ProtossGroundArmorsLevel2': 190,
    'ProtossGroundArmorsLevel3': 220,
    'ProtossShieldsLevel1': 160,
    'ProtossShieldsLevel2': 190,
    'ProtossShieldsLevel3': 220,
    'ProtossAirWeaponsLevel1': 160,
    'ProtossAirWeaponsLevel2': 190,
    'ProtossAirWeaponsLevel3': 220,
    'ProtossAirArmorsLevel1': 160,
    'ProtossAirArmorsLevel2': 190,
    'ProtossAirArmorsLevel3': 220,
    'WarpGateResearch': 160,
    'BlinkTech': 170,
    'ObserverGraviticBooster': 80,
    'GraviticDrive': 80,
    'ExtendedThermalLance': 140,
    'Charge': 140,
    'PsiStormTech': 110,
    'PhoenixRangeUpgrade': 90,
    'CarrierLaunchSpeedUpgrade': 80,
    # unit change buildings
    'Lair': 80,
    'Hive': 100,
    'GreaterSpire': 100,
    'OrbitalCommand': 35,
    'PlanetaryFortress': 50,
    'Overseer': 17,
    # LotV Alpha
    'HERC': 40,
    'ARCGun': 30,
    'TargetingOptics': 110,
    # LotV Beta
    'Cyclone': 45,  # TODO check time
    'HyperflightRotors': 130,  # TODO check name, time
    'FlyingLocusts': 120,  # TODO check name, time
    'Adept': 30, # TODO check time
    # Ravager - egg not itself because it is the start time, normal build time is ?
    'RavagerCocoon': 0,  # TODO check time
    # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is ?
    'LurkerMPEgg': 0,  # TODO check time
    'LurkerDenMP': 100,  # TODO check time
    'LurkerRange': 100,  # TODO check time
    'Disruptor': 60,  # TODO check time

}

for key, value in BUILD_TIMES.items():
    BUILD_TIMES[key] *= 16


TRACKED_ABILITIES = set([
    '250mmStrikeCannons',
    'BlindingCloud',
    'BuildAutoTurret',
    'CalldownMULE',
    'Contaminate',
    'Corruption',
    'EMPRound',
    'Feedback',
    'ForceField',
    'FungalGrowth',
    'GravitonBeam',
    'GuardianShield',
    'MassRecallMothership',
    'MothershipMassRecall',
    'MothershipCorePurifyNexus',
    'MassRecallMothershipCore',
    'InfestorNeuralParasite',
    'BuildPointDefenseDrone',
    'HallucinationArchon',
    'HallucinationColossus',
    'HallucinationHighTemplar',
    'HallucinationImmortal',
    'HallucinationPhoenix',
    'HallucinationProbe',
    'HallucinationStalker',
    'HallucinationVoidRay',
    'HallucinationWarpPrism',
    'HallucinationZealot',
    'PsionicStorm',
    'ScannerSweep',
    'SeekerMissile',
    'SniperRound',
    'SpawnLarva',
    'ExtraSupplies',
    'ChronoBoost',
    'QueenTransfusion',
    'YamatoGun',
    'Abduct',
    'TemporalField',
    'Envision',
    # LotV Beta
    'LockOn',  # TODO check name
    'TacticalJump',  # TODO check name
    'CorrosiveBile',  # TODO check name
    'CausticSpray',  # TODO check name
    'SpawnLocusts',  # TODO check name
    'Swoop',  # TODO check name
    'ParasiticBomb',  # TODO check name
    'PsionicTransfer',  # TODO check name
    'PurificationNova',  # TODO check name
    'StasisWard',  # TODO check name
    'Barrier',  # TODO check name
    'Disintegration',  # TODO check name
    'ReleaseInterceptors',  # TODO check name
    ])

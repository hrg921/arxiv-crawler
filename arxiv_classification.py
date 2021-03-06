from typing import NewType


Classification = NewType('Classification', str)

astro_physics = {
    "astrophysics": Classification('astro-ph'),
    "cosmology_and_nongalactic_astrophysics": Classification('astro-ph.CO'),
    "earth_and_planetary_astrophysics": Classification('astro-ph.EP'),
    "astrophysics_of_galaxies": Classification('astro-ph.GA'),
    "high_energy_astrophysical_phenomena": Classification('astro-ph.HE'),
    "instrumentation_and_methods_for_astrophysics": Classification('astro-ph.IM'),
    "solar_and_stellar_astrophysics": Classification('astro-ph.SR')
}

computer_science = {
        "artificial_intelligence": Classification('cs.AI'),
        "hardware_architecture": Classification('cs.AR'),
        "computational_complexity": Classification('cs.CC'),
        "computational_engineering_and_finance_and_science": Classification('cs.CE'),
        "computational_geometry": Classification('cs.CG'),
        "computation_and_language": Classification('cs.CL'),
        "cryptography_and_security": Classification('cs.CR'),
        "computer_vision_and_pattern_recognition": Classification('cs.CV'),
        "computers_and_society": Classification('cs.CY'),
        "databases": Classification('cs.DB'),
        "distributed_and_parallel_and_cluster_computing": Classification('cs.DC'),
        "digital_libraries": Classification('cs.DL'),
        "discrete_mathematics": Classification('cs.DM'),
        "data_structures_and_algorithms": Classification('cs.DS'),
        "emerging_technologies": Classification('cs.ET'),
        "formal_languages_and_automata_theory": Classification('cs.FL'),
        "general_literature": Classification('cs.GL'),
        "graphics": Classification('cs.GR'),
        "computer_science_and_game_theory": Classification('cs.GT'),
        "human_computer_interaction": Classification('cs.HC'),
        "information_retrieval": Classification('cs.IR'),
        "information_theory": Classification('cs.IT'),
        "machine_learning": Classification('cs.LG'),
        "logic_in_computer_science": Classification('cs.LO'),
        "multiagent_systems": Classification('cs.MA'),
        "multimedia": Classification('cs.MM'),
        "mathematical_software": Classification('cs.MS'),
        "numerical_analysis": Classification('cs.NA'),
        "neural_and_evolutionary_computing": Classification('cs.NE'),
        "networking_and_internet_architecture": Classification('cs.NI'),
        "other_computer_science": Classification('cs.OH'),
        "operating_systems": Classification('cs.OS'),
        "performance": Classification('cs.PF'),
        "programming_languages": Classification('cs.PL'),
        "robotics": Classification('cs.RO'),
        "symbolic_computation": Classification('cs.SC'),
        "sound": Classification('cs.SD'),
        "software_engineering": Classification('cs.SE'),
        "social_and_information_networks": Classification('cs.SI'),
        "systems_and_control": Classification('cs.SY')
}


statistics = {
    "applications": Classification('stat.AP'),
    "computation": Classification('stat.CO'),
    "methodology": Classification('stat.ME'),
    "machine_learning": Classification('stat.ML'),
    "other_statistics": Classification('stat.OT'),
    "statistics_theory": Classification('stat.TH')
}


arxiv_classification = {
    "disordered_systems_and_neural_networks": Classification('cond-mat.dis-nn'),
    "mesoscale_and_nanoscale_physics": Classification('cond-mat.mes-hall'),
    "materials_science": Classification('cond-mat.mtrl-sci'),
    "other_condensed_matter": Classification('cond-mat.other'),
    "quantum_gases": Classification('cond-mat.quant-gas'),
    "soft_condensed_matter": Classification('cond-mat.soft'),
    "statistical_mechanics": Classification('cond-mat.stat-mech'),
    "strongly_correlated_electrons": Classification('cond-mat.str-el'),
    "superconductivity": Classification('cond-mat.supr-con'),
    "econometrics": Classification('econ.EM'),
    "audio_and_speech_processing": Classification('eess.AS'),
    "image_and_video_processing": Classification('eess.IV'),
    "signal_processing": Classification('eess.SP'),
    "general_relativity_and_quantum_cosmology": Classification('gr-qc'),
    "high_energy_physics_experiment": Classification('hep-ex'),
    "high_energy_physics_lattice": Classification('hep-lat'),
    "high_energy_physics_phenomenology": Classification('hep-ph'),
    "high_energy_physics_theory": Classification('hep-th'),
    "commutative_algebra": Classification('math.AC'),
    "algebraic_geometry": Classification('math.AG'),
    "analysis_of_pdes": Classification('math.AP'),
    "algebraic_topology": Classification('math.AT'),
    "classical_analysis_and_odes": Classification('math.CA'),
    "combinatorics": Classification('math.CO'),
    "category_theory": Classification('math.CT'),
    "complex_variables": Classification('math.CV'),
    "differential_geometry": Classification('math.DG'),
    "dynamical_systems": Classification('math.DS'),
    "functional_analysis": Classification('math.FA'),
    "general_mathematics": Classification('math.GM'),
    "general_topology": Classification('math.GN'),
    "group_theory": Classification('math.GR'),
    "geometric_topology": Classification('math.GT'),
    "history_and_overview": Classification('math.HO'),
    "information_theory": Classification('math.IT'),
    "k_theory_and_homology": Classification('math.KT'),
    "logic": Classification('math.LO'),
    "metric_geometry": Classification('math.MG'),
    "mathematical_physics_MP": Classification('math.MP'),
    "numerical_analysis": Classification('math.NA'),
    "number_theory": Classification('math.NT'),
    "operator_algebras": Classification('math.OA'),
    "optimization_and_control": Classification('math.OC'),
    "probability": Classification('math.PR'),
    "quantum_algebra": Classification('math.QA'),
    "rings_and_algebras": Classification('math.RA'),
    "representation_theory": Classification('math.RT'),
    "symplectic_geometry": Classification('math.SG'),
    "spectral_theory": Classification('math.SP'),
    "statistics_theory": Classification('math.ST'),
    "mathematical_physics": Classification('math-ph'),
    "adaptation_and_self_organizing_systems": Classification('nlin.AO'),
    "chaotic_dynamics": Classification('nlin.CD'),
    "cellular_automata_and_lattice_gases": Classification('nlin.CG'),
    "pattern_formation_and_solitons": Classification('nlin.PS'),
    "exactly_solvable_and_integrable_systems": Classification('nlin.SI'),
    "nuclear_experiment": Classification('nucl-ex'),
    "nuclear_theory": Classification('nucl-th'),
    "accelerator_physics": Classification('physics.acc-ph'),
    "atmospheric_and_oceanic_physics": Classification('physics.ao-ph'),
    "applied_physics": Classification('physics.app-ph'),
    "atomic_and_molecular_clusters": Classification('physics.atm-clus'),
    "atomic_physics": Classification('physics.atom-ph'),
    "biological_physics": Classification('physics.bio-ph'),
    "chemical_physics": Classification('physics.chem-ph'),
    "classical_physics": Classification("physics.class-ph"),
    "computational_physics": Classification('physics.comp-ph'),
    "data_analysisand_statistics_and_probability": Classification('physics.data-an'),
    "physics_education": Classification('physics.ed-ph'),
    "fluid_dynamics": Classification('physics.flu-dyn'),
    "general_physics": Classification('physics.gen-ph'),
    "geophysics": Classification('physics.geo-ph'),
    "history_and_philosophy_of_physics": Classification('physics.hist-ph'),
    "instrumentation_and_detectors": Classification('physics.ins-det'),
    "medical_physics": Classification('physics.med-ph'),
    "optics": Classification('physics.optics'),
    "plasma_physics": Classification('physics.plasm-ph'),
    "popular_physics": Classification('physics.pop-ph'),
    "physics_and_society": Classification('physics.soc-ph'),
    "space_physics": Classification('physics.space-ph'),
    "biomolecules": Classification('q-bio.BM'),
    "cell_behavior": Classification('q-bio.CB'),
    "genomics": Classification('q-bio.GN'),
    "molecular_networks": Classification('q-bio.MN'),
    "neurons_and_cognition": Classification('q-bio.NC'),
    "other_quantitative_biology": Classification('q-bio.OT'),
    "populations_and_evolution": Classification('q-bio.PE'),
    "quantitative_methods": Classification('q-bio.QM'),
    "subcellular_processes": Classification('q-bio.SC'),
    "tissues_and_organs": Classification('q-bio.TO'),
    "computational_finance": Classification('q-fin.CP'),
    "economics": Classification('q-fin.EC'),
    "general_finance": Classification('q-fin.GN'),
    "mathematical_finance": Classification('q-fin.MF'),
    "portfolio_management": Classification('q-fin.PM'),
    "pricing_of_securities": Classification('q-fin.PR'),
    "risk_management": Classification('q-fin.RM'),
    "statistical_finance": Classification('q-fin.ST'),
    "trading_and_market_microstructure": Classification('q-fin.TR'),
    "quantum_physics": Classification('quant-ph')
}


def get_computer_science_category_list():
    computer_science_category_list = []
    for key, value in computer_science.items():
        computer_science_category_list.append(value)
    return computer_science_category_list


def get_statistics_category_list():
    statistics_category_list = []
    for key, value in statistics.items():
        statistics_category_list.append(value)
    return statistics_category_list


def get_all_category_list():
    category_list = []
    for key, value in arxiv_classification.items():
        category_list.append(value)
    return category_list + get_computer_science_category_list() + get_statistics_category_list()

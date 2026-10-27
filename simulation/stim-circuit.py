import stim
print(stim.__version__)

ROUNDS = 3
DISTANCE = 3 # Code-distance
NOISE = 0.01 # Physical error rate 
NUM_SHOTS = 100000 

circuit = stim.Circuit.generated(
    "surface_code:rotated_memory_z",
    rounds = ROUNDS,
    distance = DISTANCE,
    after_clifford_depolarization = NOISE,
    after_reset_flip_probability= NOISE,
    before_measure_flip_probability= NOISE,
    before_round_data_depolarization= NOISE,
)
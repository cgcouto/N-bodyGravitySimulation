import json
import numpy as np

# create n-body data
positions = np.random.rand(300,2)*200 + 400
velocities = np.random.rand(300,2)*2 - 1

# assign into arrays 
pos_x = positions[:,0]
pos_y = positions[:,1]
vel_x = velocities[:,0]
vel_y = velocities[:,1]
mass = 40.0

description = "Test cube n-body scene..."

# save out arrays to json 
name = "cube"

nbody_dict = {
    "simData" : {
        "pos_x" : pos_x.tolist(),
        "pos_y" : pos_y.tolist(),
        "vel_x" : vel_x.tolist(),
        "vel_y" : vel_y.tolist(),
        "mass" : mass
    },
    "menuContents" : {
        "description" : description
    }
}

with open('snapshots/' + name + '.json', 'w') as f:
    json.dump(nbody_dict, f)
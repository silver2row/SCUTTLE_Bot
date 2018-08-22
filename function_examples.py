# Gonna change library name to robot name

import motion

#	Turning

motion.turnForward([swing,point],value,speed)

motion.turnBackward([swing,point],value,speed)

#	Forward/Backward

# Also need to add functions for different coms types

motion.forward([rotations,distance],value,speed)

motion.backward([rotations.distance],value,speed)

#	Get Sensor Values

motion.compass(value_type)

motion.irProximity(value_type)

motion.rotaryEncoders(value_type)

motion.hbridgeTemp(value_type)

motion.hbridgeVoltage(value_type)

motion.barrelVoltage(value_type)

motion.lipoVolatage(value_type)

#	Advanced

motion.motorMessage()



################################################################################
# CSE 251B: Programming Assignment 2
# Winter 2023
# Code by Madeleine Kerr
################################################################################
# To install PyYaml, refer to the instructions for your system:
# https://pyyaml.org/wiki/PyYAMLDocumentation
################################################################################
# If you don't have NumPy installed, please use the instructions here:
# https://scipy.org/install.html
################################################################################

import gradient
from constants import *
from train import *
from gradient import *
import argparse
#import util



def main(args):
    # Read the required config
    # Create different config files for different experiments

    configFile = None  # Will contain the name of the config file to be loaded
    if (args.experiment == 'test_gradients'):  # 3b
        configFile = "config_3b.yaml"  # Create a config file for 3b and change None to the config file name
    elif (args.experiment == 'test_momentum'):  # 3c
        configFile = "config_3c.yaml"  # Create a config file for 3c and change None to the config file name
    elif (args.experiment == 'test_regularization'):  # 3d
        configFile = "config_3d.yaml"  # Create a config file for 3d and change None to the config file name
    elif (args.experiment == 'test_activation'):  # 3e
        configFile = 'config_3e.yaml'  # Create a config file for 3e and change None to the config file name
    elif (args.experiment == 'test_half_units'):  # 3f-i
        configFile = 'config_3fia.yaml'  # Create a config file for 3f-i and change None to the config file name
    elif (args.experiment == 'test_double_units'):  # 3f-i
        configFile = 'config_3fib.yaml'  # Create a config file for 3f-i and change None to the config file name
    elif (args.experiment == 'test_hidden_layers'):  # 3f-ii
        configFile = 'config_3fii.yaml'  # Create a config file for 3f-ii and change None to the config file name
    elif (args.experiment == 'test_100_classes'):  # 3g
        configFile = 'config_3g.yaml'  # Create a config file for 3g and change None to the config file name

    # Load the configuration from the corresponding yaml file. Specify the file path and name
    config = util.load_config(configYamlPath + configFile)  # Set configYamlPath, configFile  in constants.py

    # Load the data
    if config['image_type'] == 'coarse':
        x_train, y_train, x_valid, y_valid, x_test, y_test = util.load_data(
            path=datasetDir)  # Set datasetDir in constants.py
    elif config['image_type'] == 'fine':
        x_train, y_train, x_valid, y_valid, x_test, y_test = util.load_data_fine(
            path=datasetDir)  # Set datasetDir in constants.py
    else:
        raise NotImplementedError(f'image_type {config["image_type"]} not implemented')

    if (args.experiment == 'test_gradients'):
        gradient.checkGradient(x_train, y_train, config)
        return 1

    # Create a Neural Network object which will be our model
    model = Neuralnetwork(config)

    # train the model. Use train.py's train method for this
    model = train(model, x_train, y_train, x_valid, y_valid, config)

    # test the model. Use train.py's modelTest method for this
    test_acc, test_loss = modelTest(model, x_test, y_test)

    # Print test accuracy and test loss
    print('Test Accuracy:', test_acc, ' Test Loss:', test_loss)


if __name__ == "__main__":
    # Parse the input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--experiment', type=str, default='test_momentum',
                        help='Specify the experiment that you want to run')
    args = parser.parse_args()
    main(args)

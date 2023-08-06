# server-packaging

## Steps for installing and running the OSS version of Aqueduct.

0. Prerequisite: make sure you have Python 3.7, 3.8 or 3.9 installed.
1. [Recommended] create a virtual environment: `python3 -m venv <VENV_NAME> && source <VENV_NAME>/bin/activate`. Note that if you created a virtual environment, you will need to perform all steps below
within the virtual environment.
2. Make sure `pip3` is up-to-date by running `python3 -m pip install --upgrade pip`
3. `cd` into this package directory and run `pip3 install .`. This will also install the SDK.
4. Run `which aqueduct` to verify the `aqueduct` executable is on `PATH`. If not, add it to your `PATH`.
On Mac, for example, this can be done via adding `export PATH="$PATH:/PATH/TO/Python/3.x/bin"`
to `~/.bash_profile` and running `source ~/.bash_profile`.
5. To start the aqueduct server, run `aqueduct server`. The server will also print out the API key
needed when using the sdk and the UI.
6. To start the aqueduct UI, run `aqueduct ui`. Note that you need to install node js and npm in order to compile and 
run the UI. Follow the instruction [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
Also, if the client (browser) and the server aren't running on the same machine, you need to provide 
the public ip of the server when starting the UI, via `aqueduct ui <PUBLIC_IP>`.
7. To get the API key, run `aqueduct apikey`.
8. Try running the example [notebook](https://github.com/aqueducthq/aqueduct-sdk-oss/blob/main/examples/sentiment_analysis/Sentiment%20Model.ipynb) with `client = aqueduct.Client("<API_KEY>", "localhost:8080")`
9. [Optional] If you want to connect to other integrations, run `aqueduct install <INTEGRATION_NAME>`.
For example, `aqueduct install postgres`.
10. To clear all existing state, run `aqueduct clear`. You can then run `aqueduct server` and `aqueduct ui`
to start the server and the UI from fresh.
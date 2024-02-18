
## Airflow with Astro CLI

### The Astro CLI is the command line interface for data orchestration with Apache Airflow.



### Installation Commands:

#### Installation for  Linux:
--> curl -sSL install.astronomer.io | sudo bash -s

#### To install Specific Version, for Linux:
--> curl -sSL install.astronomer.io | sudo bash -s -- v1.23.0


#### Installation for  Mac:
--> brew install astro

#### To install Specific Version, for Mac:
--> brew install astro@<major.minor.patch-version>



### Create / Intialize an Astro Project inside your project root directory:
--> astro dev init



### Run/start astro cli (using docker image build)
--> astro dev start

### Restart astro cli
--> astro dev restart
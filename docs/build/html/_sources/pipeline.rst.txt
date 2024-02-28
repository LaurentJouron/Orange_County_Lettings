.. _pipeline:

**Pipelines**
============

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******************
Spin up environment
*******************

📜 Build-agent:
   * Specifies the version of the CircleCI build agent used to run the build.

📜 System information: 
   * Provides information about the operating system and construction environment. In our case, the operating system is Ubuntu 20.04.6 LTS, with a Linux kernel 5.15.0-1053-aws.

📜 Starting container: 
   * Indicates the start of a Docker container based on the cimg/python:3.12.0 image, necessary to execute the construction steps.

📜 Warning: No authentication provided: 
   * This warning indicates that no authentication has been provided to pull the image from Docker Hub. CircleCI uses its own credentials for this.

📜 Image cache not found on this host, downloading cimg/python:3.12.0:
   * Indicates that the Docker cimg/python:3.12.0 image is not present in the local cache of the build host and must therefore be downloaded from the Docker Hub.

📜 cimg/python:3.12.0: 
   * Detailed information about the downloaded Docker image, including its SHA256 hash.

📜 Pull stats: 
   * Statistics on downloading and extracting the Docker image, indicating the time required and the download speed.

📜 Time to create container: 
   * Time required to create the Docker container from the uploaded image.

📜 Time to upload agent and config: 
   * Time required to download the build agent and configuration file.

📜 Time to start containers: 
   * The time it takes to start Docker containers to complete the construction steps.

This release provides an overview of the CircleCI build environment startup process and the download of dependencies needed to run the build steps.

.. figure:: _static/circleci_spin_up_environnement.png
   :scale: 50
   :align: center
   :alt: circleci spin up environnement

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/circleci_spin_up_environnement.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*******************************
Preparing environment variables
*******************************

📜 Construction environment variables: BASH_ENV, CIRCLECI, CI, etc...:

   * These variables are defined by the CircleCI build environment to provide information about the current process. 

   * Example

      * CIRCLE_BRANCH contains the name of the current branch (master in this case), 
      * CIRCLE_BUILD_NUM contains the build number
      * CIRCLE_BUILD_URL provides the URL of the build details page on the CircleCI dashboard.

📜 Project environment variables: CIRCLE_USERNAME, CIRCLE_PROJECT_REPONAME, CIRCLE_REPOSITORY_URL, etc...:

   * These variables are derived from the CircleCI project parameters and provide specific information about the project under construction.

   * Example

      * CIRCLE_USERNAME contains the project owner username, 
      * CIRCLE_PROJECT_REPONAME contains the repository name
      * CIRCLE_REPOSITORY_URL contains the Git repository URL.

📜 Workflow environment variables: CIRCLE_WORKFLOW_ID, CIRCLE_WORKFLOW_JOB_ID, etc...:

   * These variables are associated with the running workflow. They provide information about the workflow ID, the job ID in the workflow, and the workflow workspace ID.


📜 Other variables: CIRCLE_OIDC_TOKEN, CIRCLE_OIDC_TOKEN_V2, CIRCLE_PLUGIN_TEST:

   * These variables are project-specific and can be used to store sensitive information or API keys. In this case, they are redacted (**REDACTED**) for security reasons. This pipeline appears to be a build and test (build_and_test) phase of your Orange County Lettings project. It is triggered on the master branch and uses various environment variables to retrieve information about the context of the build.

.. figure:: _static/circleci_preparing_enrironnment_variables.png
   :scale: 50
   :align: center
   :alt: circleci preparing enrironnment variables

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/circleci_preparing_enrironnment_variables.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📜 Checkout code

   * This part of the build output is related to the configuration and use of SSH keys to access Git repositories.


📜 Creating .ssh directory: 

   * Creates the . ssh directory in the user directory to store the SSH keys.

📜 Adding the following entries to known_hosts:

   * Added Git host public key (GitHub, Bitbucket, GitLab) to known_hosts file. This allows the trusted host (CircleCI) to identify the Git host and ensure that it connects to the correct server.

📜 Writing SSH key for checkout:

   * Generates a private SSH key (id_rsa) and a public key (id_rsa.pub) for authentication when retrieving source code from the Git repository.

📜 Cloning git repository : 

   * Clone the Git repository to the current working directory.

📜 Checking out branch : 

   * Checks the specified branch. In this case, it is mentioned that the branch is up to date with origin/master and that the HEAD is now on the latest revision of this branch.


These steps ensure that CircleCI can access the Git repository using SSH keys and retrieve the source code for construction.

.. figure:: _static/circleci_checkout_code.png
   :scale: 50
   :align: center
   :alt: circleci checkout code

.. raw:: html

   <div style="text-align: center;">
       <a href="_static/circleci_checkout_code.png" download class="button">
          <img src="_static/button_download.png" alt="Donwload button" width="100" height="50" />
       </a>
   </div>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. raw:: html

   <a href="https://app.circleci.com/pipelines/github/LaurentJouron/Orange_County_Lettings" class="button">
       <img src="_static/button_all_pipelines.png" alt="Report button" width="200" height="100" />
   </a>

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
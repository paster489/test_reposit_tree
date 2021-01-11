# SBatch

theme:
  name: TTT
  palette:
    primary: indigo
For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Example of SBatch Script

    #!/bin/bash     
    # SBATCH --partition TBD          ## specify partition name where to run a job.
    # SBATCH --time 12:00:00          ## limit the time of job running. Format: D-H:MM:SS
    #SBATCH --job-name my_job         ## name of the job. replace my_job with your desired
                                      ## job name
    #SBATCH --output my_job-id-%J.out ## output log for running job - %J is the job number
                                      ## variable
    #SBATCH --gres=gpu:1              ## number of GPUs
    module load anaconda              ## load anaconda module
    source activate my_env            ## activating environment
    jupyter lab                       ## execute jupyter lab command

    Roses are <span style="color:red">red</span>
    Roses are <span style="color:blue;">red</span>

    ```
    python
    def fn():
      pass
    ```
    - == This ==
    --this--
    ++added++
    ~~one~~

|First Header      | Second Header    | Third Header
|:---------------- | :---------------:| ---------------:
|Content Cell      | Content Cell     | Content Cell
|Content Cell      | Content Cell     | Content Cell



## Flags Description

      mkdocs.yml    # The configuration file.
      docs/
      index.md  # The documentation homepage.
      ...       # Other markdown pages, images and other files.

## Submit Job

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Check Status of Job

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Cancel Job

      mkdocs.yml    # The configuration file.
      docs/
      index.md  # The documentation homepage.
      ...       # Other markdown pages, images and other files.

# Commands

For the summary of Slurm commands please see the link - [summary](https://slurm.schedmd.com/pdfs/summary.pdf).


## Job's Status/Resources Reports

Status:

    $ squeue -l -u$USER</span>

Details:  

    $ scontrol show job <job-id>

The maximal used memory for the _completed_ job:  

    $ sacct -j <job-id> --format=MaxRSS

Format options:  

    $ sacct -e

Maximal used memory for the _running_ job:

    $ sstat -j <job-id> --format=MaxRSS

When the job will start:

    $ squeue --start

Report status every 60 seconds:

    $ squeue -i60

You can use the script "jobinfo" from GitHub [slurm-util](https://github.com/birc-aeh/slurm-utils) site for monitoring your job:

    $ jobinfo <job-id>

## Information about computer nodes:

    $ sinfo

More details:

    $ sinfo -Nel


## Job's priority

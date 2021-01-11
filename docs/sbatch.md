# SBatch
  <span style="color:purple">#SBATCH</span> - Bash "sees" this as comment.<br/>
  <span style="color:purple">#SBATCH</span> - Bash "sees" this as comment.<br/>
  <span style="color:purple">#SBATCH</span> - Slurm "takes" them as parameter.<br/>
  Use ## to close <span style="color:purple">#SBATCH</span> as comment.<br/>


## Example of SBatch Script
  ![Screenshot](sbatch_example.png)

## Flags Description

| **Flag** <div style="width:350px">property</div> | **Description** <div style="width:100px">property</div> | **Default** |
|:----------------|:-------------|:---------------|
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">partition</span>=<ins>TBD</ins> | Partition name.  | <ins>TBD</ins> |  
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">time</span>=0-12:00:00 | Limit the time of job running. Format: D-H:MM:SS.  | <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">job-name</span>=my_job | Name of the job. Replace my_job with your desired job name. | |   
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">output</span>=%a_my_name-%J.out| Output log for running job, %J – job #, %a – run #.| |    
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">mail-user</span>=username@post.bgu.ac.il| Users email for sending job status notifications.| |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">mail-type</span>=BEGIN,END,FAIL| Conditions when to send the email. ALL,BEGIN,END,FAIL, REQUEU, NONE.| |  
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">nodelist</span>=<ins>TBD</ins>  | Specify the computer to run the job. | <ins>TBD</ins> |  
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">array</span>=1-10  | Run parallel 10 times. | <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">mem</span>=72G  | Allocate extra memory. | <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">gres</span>=gpu:1  | Number of GPUs (can't exceed 8 gpus for now) ask for more than 1 only if you can parallelize your code for multi GPU. | <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">nodes</span>=1-1 | Allocate 1 node. | <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">ntasks</span>=12  |Allocate 12 tasks| <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">cpus-per-task</span>=32  |Allocate extra CPU: 32 CPU per task.| <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">requeue</span>=32  |Re-run the task if it was preempted.| <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">dependency</span>=after(ok/notok/any):<job_ids>  |Ordering of jobs.| <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> --<span style="color:red">exclusive</span>=<user>  |To reserve a whole node for yourself, slurm will reserve a full node for the first job to start in the array, and then will schedule all the others on the same machine as only your jobs will be allowed there.| <ins>TBD</ins> |
| | | |
| <span style="color:purple">#SBATCH</span> <span style="color:red">%j</span>  |Job #.| |
| | | |
| <span style="color:purple">#SBATCH</span> <span style="color:red">%A</span>  |Value of SLURM_ARRAY_JOB_ID.| |
| | | |
| <span style="color:purple">#SBATCH</span> <span style="color:red">%a</span>  |Value of SLURM_ARRAY_TASK_ID.| |

<br/>


## Submit Job
    $ sbatch ./submit.sh
    $ sbatch --qos=name ./submit.sh

## Cancel Job

    $ cancel <job-id>

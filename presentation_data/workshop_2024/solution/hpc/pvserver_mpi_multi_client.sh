#!/bin/bash
#SBATCH --job-name=mpvserver
#SBATCH --time=0:60:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=30
#SBATCH --mem=64GB
#SBATCH --qos=normal

#SBATCH --account=ec232

module --quiet purge  # Reset the modules to the system default
module load ParaView/5.11.1-foss-2022a-mpi

mpirun --map-by ppr:1:core --bind-to core -np 50 pvserver --server-port=5556 --multi-clients

#! /bin/bash

input_dir=$1

source activate Pano3D

cd /home/lmf/Deploy/MVPFDeepPanoContext

cp /home/lmf/Deploy/MVPFDeepPanoContext/demo/input/metadata.json $input_dir

CUDA_VISIBLE_DEVICES=0 WANDB_MODE=dryrun python main.py configs/pano3d_igibson.yaml --model.scene_gcn.relation_adjust True --mode test --demo_path $input_dir

deep_output_path=$(cat /home/lmf/tmp/deep_output_path)

deep_output_scene=$deep_output_path/visualization/Merom_1_int-00009/scene.glb

cp $deep_output_scene /home/lmf/www/lab724/

echo $deep_output_scene

cd $(dirname $0)

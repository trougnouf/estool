export OMPI_MCA_rmaps_base_oversubscribe=1
timeout -sHUP 5m python train.py bullet_kuka_grasping -o ses -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_kuka_grasping -o ga -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_kuka_grasping -o cma -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_kuka_grasping -o pepg -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_kuka_grasping -o oes -n 8 -t 4
sleep 10

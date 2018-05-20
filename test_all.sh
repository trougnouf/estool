export OMPI_MCA_rmaps_base_oversubscribe=1
timeout -sHUP 100m python train.py bullet_ant -o ses -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_ant -o ga -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_ant -o cma -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_ant -o pepg -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_ant -o oes -n 8 -t 4
sleep 10
timeout -sHUP 15m python train.py bullet_racecar -o ses -n 8 -t 4
sleep 10
timeout -sHUP 15m python train.py bullet_racecar -o ga -n 8 -t 4
sleep 10
timeout -sHUP 15m python train.py bullet_racecar -o cma -n 8 -t 4
sleep 10
timeout -sHUP 15m python train.py bullet_racecar -o pepg -n 8 -t 4
sleep 10
timeout -sHUP 15m python train.py bullet_racecar -o oes -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_kuka_grasping -o ses -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_kuka_grasping -o ga -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_kuka_grasping -o cma -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_kuka_grasping -o pepg -n 8 -t 4
sleep 10
timeout -sHUP 100m python train.py bullet_kuka_grasping -o oes -n 8 -t 4
sleep 10

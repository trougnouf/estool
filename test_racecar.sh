export OMPI_MCA_rmaps_base_oversubscribe=1
timeout -sHUP 5m python train.py bullet_racecar -o ses -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_racecar -o ga -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_racecar -o cma -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_racecar -o pepg -n 8 -t 4
sleep 10
timeout -sHUP 5m python train.py bullet_racecar -o oes -n 8 -t 4
sleep 10

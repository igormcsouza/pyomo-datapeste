docker run --rm -it \
--network='host' \
-v `pwd`/notebooks:/workdir/notebooks \
igormcsouza/python-opt-tools:pyomo-datapeste \
jupyter notebook --allow-root
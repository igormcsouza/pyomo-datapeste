docker run --rm -it \
--network='host' \
-v `pwd`/notebook:/workdir/notebook \
igormcsouza/python-opt-tools:pyomo-datapeste \
jupyter notebook --allow-root
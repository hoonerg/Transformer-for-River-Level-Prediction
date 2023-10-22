# Transformer-for-River-Level-Prediction
Transformer for River Level Prediction

# Structure
River level data ---------> 
Dam discharge data ------->  Model -----> River level prediction
Rainfall station data ---->

# Models
  1.Corrformer (Transformer with Multi-Correlation mechanism)
  2.DLinear
  3.NLinear
  4.Linear


# Acknowledgement
https://github.com/thuml/Corrformer
https://github.com/cure-lab/LTSF-Linear


# Model Parameter
river_dam_rain
  --enc_in 4 \
  --dec_in 4 \
  --c_out 4 \
  --node_num 36 \
  --node_list 3,12 \

river_dam
  --enc_in 10 \
  --dec_in 10 \
  --c_out 10 \
  --node_num 11 \
  --node_list 11 \

river
  --enc_in 6 \
  --dec_in 6 \
  --c_out 6 \
  --node_num 17 \
  --node_list 17 \
# Transformer-for-River-Level-Prediction
Transformer for River Level Prediction <br/>

## Structure
| Input Data            | Process | Output                   |
|-----------------------|---------|--------------------------|
| River level data      |         |                          |
| Dam discharge data    |  --->   | River level prediction   |
| Rainfall station data |         |                          |

### Models
  1.Corrformer (Transformer with Multi-Correlation mechanism) <br/>
  2.DLinear <br/>
  3.NLinear <br/>
  4.Linear <br/>


#### Acknowledgement
https://github.com/thuml/Corrformer <br/>
https://github.com/cure-lab/LTSF-Linear <br/>


##### Model Parameter
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
model_name=DLinear

python -u ./run_longExp.py \
  --is_training 0 \
  --root_path /mnt/workspace/MyCanvas/LTSF_Linear/data/ \
  --data_path None \
  --model_id jamsu \
  --model $model_name \
  --data Jamsu \
  --patience 5 \
  --seq_len 48 \
  --label_len 24 \
  --pred_len 24 \
  --enc_in 1 \
  --des 'Exp' \
  --itr 1 \
  --batch_size 1 \
  --feature S
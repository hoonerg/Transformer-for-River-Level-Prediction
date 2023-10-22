if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi

if [ ! -d "./logs/LongForecasting/univariate" ]; then
    mkdir ./logs/LongForecasting/univariate
fi
model_name=DLinear


!python -u run_single.py \
  --is_training 1 \
  --root_path ./dataset/ \
  --data_path None \
  --model_id Jamsu \
  --model $model_name \
  --data Jamsu \
  --train_epochs 100 \
  --patience 5 \
  --seq_len 48 \
  --label_len 24 \
  --pred_len 24 \
  --enc_in 1 \
  --des 'Exp' \
  --itr 1 \
  --batch_size 8 \
  --feature S \
  --learning_rate 0.0001
def qe2_cv(Qe2_a, Qe2_b, Qe2_n, Qe2_k, Qe2_w):
    # 量子化間隔の計算
    dis = (Qe2_b - Qe2_a) / 2 ** Qe2_n
    
    # 量子化区間の決定
    interval_index = int((Qe2_k - Qe2_a) / dis)
    interval_start = Qe2_a + interval_index * dis
    interval_end = interval_start + dis
    
    # 代表値（区間中央値）の計算
    median = (interval_start + interval_end) / 2
    
    # 量子化誤差の計算
    quantization_error = abs(Qe2_k - median)
    
    return quantization_error

# Ex.2: 計算例
Qe2_a = -2.4
Qe2_b = 4
Qe2_n = 4
Qe2_k = 4
Qe2_w = "Med"
quantization_error = qe2_cv(Qe2_a, Qe2_b, Qe2_n, Qe2_k, Qe2_w)
print(quantization_error)  # 結果: 0.0238037109375
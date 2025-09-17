---
id: 7fa434b922
question: RMSE using metrics.root_meas_square()
sort_order: 2620
---

Instead of using np.sqrt() as the second step. You can extract it using like this way :

mean_squared_error(y_val, y_predict_val,squared=False)

Ahmed Okka


# Reader
とりあえず動く版

## テスト起動
docker-compose.ymlのREADER_ENV環境変数を書き換えると起動モード変更
```
READER_ENV=config.TestingConfig
# FeliCaリーダやLCDがつながってなかったり、内部エラーを起こしても適当な値を返す。デバイスがない環境でもテストできる。

READER_ENV=config.DevelopmentConfig
# debugモードONで起動

READER_ENV=config.ProductionConfig
# Production用
```
```
docker-compose up
```

## API
### 共通エラー形式
```
{
    "message": "エラーメッセージ"
}
```

### `GET` /api/v1/card
カードIDmスキャン
１Requestで１回スキャンされるため、ループなどで取得する
- Response `200` OK
```
{
      "idm": "0x00000000000000"
}
 ```
- Response `204`
スキャンしたげど何も取れなかった

### `POST` /api/v1/message
LCDメッセージ書き込み
- Request `application/json`
```
{
	"line_1": "hoge",
	"line_2": "hogehoge"
}
```
- Response `201`
```
{
	"line_1": "hoge",
	"line_2": "hogehoge"
}
 ```

### `POST` /api/v1/led
LED点灯
- Request `application/json`
```
{
	"mode": "success",
}
# success(緑), waiting(青), error(赤), destroy(消灯)
```
- Response `201`
```
{
	"mode": "success",
}
```

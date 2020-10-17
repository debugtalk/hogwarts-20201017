
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMubuLogin(HttpRunner):

    config = (
        Config("testcase description")
        .variables(
            **{
                "host": "mubu.com",
                "phone": "18912343458",
                "password": "123456",
            }
        )
        .base_url("https://$host")
        .export("data_unique_id", "JwtToken", "user_persistence")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("/")
            .get("/")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .extract()
            .with_jmespath("cookies.data_unique_id", "data_unique_id")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login")
            .get("/login")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "SLARDAR_WEB_ID": "4c3231c1-82f0-4ca9-aa6f-ba8a44743ec6",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login/password")
            .get("/login/password")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://${host}/login",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "_gat": "1",
                    "SLARDAR_WEB_ID": "6ef02f1c-9246-4e86-a356-cc448f3ebbb2",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/login/submit")
            .with_variables(**{
                "remember": "true",
                "timestamp": "${get_timestamp()}"
            })
            .post("/api/login/submit")
            .with_headers(
                **{
                    "content-length": "65",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "x-requested-with": "XMLHttpRequest",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/login/password",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "SLARDAR_WEB_ID": "51caeefc-7841-444f-913f-eb93ed088a92",
                }
            )
            .with_data(
                {
                    "phone": "$phone",
                    "password": "$password",
                    "remember": "$remember",
                    "token": "${gen_token($phone, $password, $timestamp)}"
                }
            )
            .teardown_hook("${sleep(1)}")
            .extract()
            .with_jmespath('cookies."Jwt-Token"', "JwtToken")
            .with_jmespath("cookies.user_persistence", "user_persistence")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
            .assert_equal("body.data.next", "/list")
        ),
        Step(
            RunRequest("/list")
            .get("/list")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://${host}/login/password",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "_gat": "1",
                    "SLARDAR_WEB_ID": "51caeefc-7841-444f-913f-eb93ed088a92",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1602915025",
                    "Jwt-Token": "${JwtToken}",
                    "user_persistence": "${user_persistence}",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/list/tip_new_update")
            .post("/api/list/tip_new_update")
            .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-requested-with": "XMLHttpRequest",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/list",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "_gat": "1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1602915025",
                    "Jwt-Token": "${JwtToken}",
                    "user_persistence": "${user_persistence}",
                    "SLARDAR_WEB_ID": "8365d4b0-786b-4509-a35d-5102202f6f75",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/api/list/get")
            .post("/api/list/get")
            .with_headers(
                **{
                    "content-length": "38",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "x-requested-with": "XMLHttpRequest",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/list",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "_gat": "1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1602915025",
                    "Jwt-Token": "${JwtToken}",
                    "user_persistence": "${user_persistence}",
                    "SLARDAR_WEB_ID": "8365d4b0-786b-4509-a35d-5102202f6f75",
                }
            )
            .with_data({"folderId": "0", "sort": "name", "keywords": "", "source": ""})
            .teardown_hook("${get_folders_num($response)}", "folders_num")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
            .assert_length_greater_than("body.data.folders", 5)
            .assert_greater_than("$folders_num", 5)
        ),
        Step(
            RunRequest("/api/message/get_message_unread")
            .post("/api/message/get_message_unread")
            .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-requested-with": "XMLHttpRequest",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/list",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "_gat": "1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1602915025",
                    "Jwt-Token": "${JwtToken}",
                    "user_persistence": "${user_persistence}",
                    "SLARDAR_WEB_ID": "8365d4b0-786b-4509-a35d-5102202f6f75",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/api/list/fg_config")
            .post("/api/list/fg_config")
            .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-requested-with": "XMLHttpRequest",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/list",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    "language": "en-US",
                    "country": "US",
                    "_gat": "1",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1602915025",
                    "Jwt-Token": "${JwtToken}",
                    "user_persistence": "${user_persistence}",
                    "SLARDAR_WEB_ID": "8365d4b0-786b-4509-a35d-5102202f6f75",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
            .assert_equal("body.data", "100")
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuLogin().test_start()

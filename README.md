# Fuck Gewu

让你快快乐乐的做物理实验.

## API 说明

```python3
login(username, password)

username: 学号
password: 密码
```

登录网页并返回认证所需的Cookie: PHPSESSION, 此session可用于网页跳转.

> 该session并不过期


```python3
fuckUp(cookie, target, key, final)

cookie: 认证所需cookie
target: 期望访问的目标路由
key: 搜索所用的报告关键字
final: 储存路由与对应分数的全局字典
```
> 次方法一次返回一个页面信息,因此使用进程池并发请求.


```python3
getScore(resp, target)

resp: 请求页面的返回包
target: 期望访问的目标路由
```
> 该方法返回对应报告的**第一作者**的姓名与学号(都是我的)


```python3
getScore(resp, target)

resp: 请求页面返回包
target: 期望访问的目标路由
```
> 该方法返回对应报告的得分情况, 若未批阅则跳过.好像有点bug,有的分数拉不到...

```python3
parseScore(final)

final: 储存对应报告与分数的字典
```
> 根据分数进行排序,感觉可能没必要?...


```python3
main(username, passwrod, start, end, key)

start: 路由开始的位置
end: 路由结束的位置
key: 关键字
```
> 使用进程池进行搜索, 调用fuckUp进行遍历. 测试时可用test()函数.

---

## TODO

1. 数据存入数据库
	- 路由值
	- 分数
	- 姓名
	- 学号

2. 可自动跳转
	 - 这个比较简单, 首先用js把PHPSESSION添加到cookie中,然后在标签中添加超链接就可以免登录跳转了(思路大概如此)

3. 实时更新页面数据
	 - 至于UI的话......大概可以一个报告对应一个card? 然后按分数排序显示

4. 自动组装报告
	- 真不是人啊












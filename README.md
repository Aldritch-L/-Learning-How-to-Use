# 怎么用vscode和git/github多人修订教材
这是个学习用实验性文件

第一步（已完成） 从GitHub上将新建的项目clone到本地
第二步 搞清楚Git的基本流程，包括add, commit, push, pull
第三步 搞清楚多人协作的流程


过程记录：
· 记录1：
    add的过程没问题，但是push出现问题
    √ 已解决
    原因未知，疑似网络状态不稳定

· 记录2：
    add, push过程已能跑通，但commit, pull不知怎么去弄

· 记录3：
    尝试使用.gitigonre来隐藏一些文件不push

· 记录4：
    在消息框中输入first commit后应该是成功实现了commit步骤，但是在后续的push中出现问题，无法同步到GitHub上，疑似还是网络问题
    尝试不使用commit直接同步更改
    √ 已解决
    原因为VPN不契合，用VS同步到GitHub的操作需断开VPN进行，但访问GitHub（登陆网站）查看更改成功与否又需要挂上VPN

· 记录5：
    在修改完第一次之后add，之后不进行commit或push操作，直接对文件二次修改，查看有何不同
    √ 已确认
    会在更改模块中多出一个版本的文件，再次add后，会覆盖暂存的版本
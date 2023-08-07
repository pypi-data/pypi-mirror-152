# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 0:52
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
import nonebot
from nonebot import on_command, logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.adapters.onebot.v11.exception import ActionFailed
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER
from . import approve
from .utils import At, banSb, init, check_func_status
from .group_request_verify import verify
from . import approve, group_request_verify, group_request, notice, utils, word_analyze, r18_pic_ban, auto_ban, switcher
from .config import plugin_config

cb_notice = plugin_config.callback_notice

admin_init =  on_command('群管初始化', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)


@admin_init.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    await init()

ban = on_command('禁', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)


@ban.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /禁 @user 禁言
    """
    msg = str(event.get_message()).replace(" ", "").split("]")
    sb = At(event.json())
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            if len(msg) > len(sb) and msg[-1] != "":
                try:
                    time = int(msg[-1:][0])
                except ValueError:
                    for q in sb:
                        raw_msg = event.raw_message.replace(" ", "").replace(str(q), "")
                    time = int(''.join(str(num) for num in list(filter(lambda x: x.isdigit(), raw_msg))))
                baning = banSb(gid, ban_list=sb, time=time)
                async for baned in baning:
                    if baned:
                        try:
                            await baned
                        except ActionFailed:
                            await ban.finish("权限不足")
                        else:
                            logger.info("禁言操作成功")
                            if cb_notice:
                                await ban.finish("禁言操作成功")
            else:
                baning = banSb(gid, ban_list=sb)
                async for baned in baning:
                    if baned:
                        try:
                            await baned
                        except ActionFailed:
                            await ban.finish("权限不足")
                        else:
                            logger.info("禁言操作成功")
                            if cb_notice:
                                await ban.finish("禁言操作成功")
                    await ban.send(f"该用户已被禁言随机时长")
        else:
            pass
    else:
        await ban.send(f"功能处于关闭状态，发送【开关管理】开启")


unban = on_command("解", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)


@unban.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /解 @user 解禁
    """
    msg = str(event.get_message())
    sb = At(event.json())
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            # if len(msg.split()) == len(sb):
            baning = banSb(gid, ban_list=sb, time=0)
            async for baned in baning:
                if baned:
                    try:
                        await baned
                    except ActionFailed:
                        await unban.finish("权限不足")
                    else:
                        logger.info("解禁操作成功")
                        if cb_notice:
                            await unban.finish("解禁操作成功")
    else:
        await unban.send(f"功能处于关闭状态，发送【开关管理】开启")


ban_all = on_command("/all", permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@ban_all.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    （测试时没用..）
    /all 全员禁言
    /all  解 关闭全员禁言
    """
    msg = event.get_message()
    if msg and '解' in str(msg):
        enable = False
    else:
        enable = True
    try:
        await bot.set_group_whole_ban(
            group_id=event.group_id,
            enable=enable
        )
    except ActionFailed:
        await ban_all.finish("权限不足")
    else:
        logger.info(f"全体操作成功 {str(enable)}")
        if cb_notice:
            await ban_all.finish(f"全体操作成功 {str(enable)}")


change = on_command('改', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@change.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /改 @user xxx 改群昵称
    """
    msg = str(event.get_message())
    logger.info(msg.split())
    sb = At(event.json())
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            try:
                for user_ in sb:
                    await bot.set_group_card(
                        group_id=gid,
                        user_id=int(user_),
                        card=msg.split()[-1:][0]
                    )
            except ActionFailed:
                await change.finish("权限不足")
            else:
                logger.info("改名片操作成功")
                if cb_notice:
                    await change.finish("改名片操作成功")
    else:
        await change.send(f"功能处于关闭状态，发送【开关管理】开启")


title = on_command('头衔', permission=SUPERUSER | GROUP_OWNER, priority=1, block=True)


@title.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /头衔 @user  xxx  给某人头衔
    """
    msg = str(event.get_message())
    stitle = msg.split()[-1:][0]
    logger.info(str(msg.split()), stitle)
    sb = At(event.json())
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            if 'all' not in sb:
                try:
                    for qq in sb:
                        await bot.set_group_special_title(
                            group_id=gid,
                            user_id=int(qq),
                            special_title=stitle,
                            duration=-1,
                        )
                except ActionFailed:
                    await title.finish("权限不足")
                else:
                    logger.info(f"改头衔操作成功{stitle}")
                    if cb_notice:
                        await title.finish(f"改头衔操作成功{stitle}")
            else:
                await title.finish("未填写头衔名称 或 不能含有@全体成员")
    else:
        await title.send(f"功能处于关闭状态，发送【开关管理】开启")


title_ = on_command('删头衔', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@title_.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /删头衔 @user 删除头衔
    """
    msg = str(event.get_message())
    stitle = msg.split()[-1:][0]
    logger.info(str(msg.split()), stitle)
    sb = At(event.json())
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            if 'all' not in sb:
                try:
                    for qq in sb:
                        await bot.set_group_special_title(
                            group_id=gid,
                            user_id=int(qq),
                            special_title="",
                            duration=-1,
                        )
                except ActionFailed:
                    await title_.finish("权限不足")
                else:
                    logger.info(f"改头衔操作成功{stitle}")
                    if cb_notice:
                        await title_.finish(f"改头衔操作成功{stitle}")
            else:
                await title_.finish("有什么输入错误 或 不能含有@全体成员")
    else:
        await title_.send(f"功能处于关闭状态，发送【开关管理】开启")


kick = on_command('踢', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@kick.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /踢 @user 踢出某人
    """
    msg = str(event.get_message())
    sb = At(event.json())
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            if 'all' not in sb:
                try:
                    for qq in sb:
                        await bot.set_group_kick(
                            group_id=gid,
                            user_id=int(qq),
                            reject_add_request=False
                        )
                except ActionFailed:
                    await kick.finish("权限不足")
                else:
                    logger.info(f"踢人操作成功")
                    if cb_notice:
                        await kick.finish(f"踢人操作成功")
            else:
                await kick.finish("不能含有@全体成员")
    else:
        await kick.send(f"功能处于关闭状态，发送【开关管理】开启")


kick_ = on_command('黑', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@kick_.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    黑 @user 踢出并拉黑某人
    """
    msg = str(event.get_message())
    sb = At(event.json())
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            if 'all' not in sb:
                try:
                    for qq in sb:
                        await bot.set_group_kick(
                            group_id=gid,
                            user_id=int(qq),
                            reject_add_request=True
                        )
                except ActionFailed:
                    await kick_.finish("权限不足")
                else:
                    logger.info(f"踢人并拉黑操作成功")
                    if cb_notice:
                        await kick_.finish(f"踢人并拉黑操作成功")
            else:
                await kick_.finish("不能含有@全体成员")
    else:
        await kick_.send(f"功能处于关闭状态，发送【开关管理】开启")


set_g_admin = on_command("管理员+", permission=SUPERUSER | GROUP_OWNER, priority=1, block=True)


@set_g_admin.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    管理员+ @user 添加群管理员
    """
    msg = str(event.get_message())
    logger.info(msg)
    logger.info(msg.split())
    sb = At(event.json())
    logger.info(sb)
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            if 'all' not in sb:
                try:
                    for qq in sb:
                        await bot.set_group_admin(
                            group_id=gid,
                            user_id=int(qq),
                            enable=True
                        )
                except ActionFailed:
                    await set_g_admin.finish("权限不足")
                else:
                    logger.info(f"设置管理员操作成功")
                    await set_g_admin.finish("设置管理员操作成功")
            else:
                await set_g_admin.finish("指令不正确 或 不能含有@全体成员")
    else:
        await set_g_admin.send(f"功能处于关闭状态，发送【开关管理】开启")


unset_g_admin = on_command("管理员-", permission=SUPERUSER | GROUP_OWNER, priority=1, block=True)


@unset_g_admin.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    管理员+ @user 添加群管理员
    """
    msg = str(event.get_message())
    logger.info(msg)
    logger.info(msg.split())
    sb = At(event.json())
    logger.info(sb)
    gid = event.group_id
    status = await check_func_status("admin", str(gid))
    if status:
        if sb:
            if 'all' not in sb:
                try:
                    for qq in sb:
                        await bot.set_group_admin(
                            group_id=gid,
                            user_id=int(qq),
                            enable=False
                        )
                except ActionFailed:
                    await unset_g_admin.finish("权限不足")
                else:
                    logger.info(f"取消管理员操作成功")
                    await unset_g_admin.finish("取消管理员操作成功")
            else:
                await unset_g_admin.finish("指令不正确 或 不能含有@全体成员")
    else:
        await unset_g_admin.send(f"功能处于关闭状态，发送【开关管理】开启")


__usage__ = """
【初始化】：
  群管初始化 ：初始化插件

【群管】：
权限：permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER
  禁言:
    禁 @某人 时间（s）[1,2591999]
    禁 时间（s）@某人 [1,2591999]
    禁 @某人 缺省时间则随机
    禁 @某人 0 可解禁
    解 @某人
  全群禁言（好像没用？）
    /all 
    /all 解
  改名片
    改 @某人 名片
  改头衔
    头衔 @某人 头衔
    删头衔
  踢出：
    踢 @某人
  踢出并拉黑：
   黑 @某人
   
【管理员】permission=SUPERUSER | GROUP_OWNER
  管理员+ @xxx 设置某人为管理员
  管理员- @xxx 取消某人管理员
  
【加群自动审批】：
群内发送 permission=GROUP_ADMIN | GROUP_OWNER | SUPERUSER
  查看词条 ： 查看本群审批词条   或/审批
  词条+ [词条] ：增加审批词条 或/审批+
  词条- [词条] ：删除审批词条 或/审批-

【superuser】：
  所有词条 ：  查看所有审批词条   或/su审批
  指定词条+ [群号] [词条] ：增加指定群审批词条 或/su审批+
  指定词条- [群号] [词条] ：删除指定群审批词条 或/su审批-
  自动审批处理结果将发送给superuser

【分群管理员设置】*分管：可以接受加群处理结果消息的用户
群内发送 permission=GROUP_ADMIN | GROUP_OWNER | SUPERUSER
  分管+ [user] ：user可用@或qq 添加分群管理员
  分管- [user] ：删除分群管理员
  查看分管 ：查看本群分群管理员

群内或私聊 permission=SUPERUSER
  所有分管 ：查看所有分群管理员
  群管接收 ：打开或关闭超管消息接收（关闭则审批结果不会发送给superusers）
  
【群词云统计】
该功能所用库 wordcloud 未写入依赖，请自行安装
群内发送：
  记录本群 ： 开始统计聊天记录 permission=GROUP_ADMIN | GROUP_OWNER | SUPERUSER
  停止记录本群 ：停止统计聊天记录
  群词云 ： 发送词云图片
  
【被动识别】
涩图检测：将禁言随机时间

违禁词检测：已支持正则表达式，可定义触发违禁词操作(默认为禁言+撤回)
定义操作方法：用制表符分隔，左边为触发条件，右边为操作定义($禁言、$撤回)
群内发送：
  简单违禁词 ：简单级别过滤
  严格违禁词 ：严格级别过滤(不建议)
  更新违禁词库 ：手动更新词库
    违禁词库每周一自动更新
    
【功能开关】
群内发送：
  开关xx : 对某功能进行开/关  permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER
  开关状态 ： 查看各功能的状态
  xx in ：
    ['管理', '踢', '禁', '改', '基础群管']  #基础功能 踢、禁、改、管理员+-
    ['加群', '审批', '加群审批', '自动审批'] #加群审批
    ['词云', '群词云', 'wordcloud'] #群词云
    ['违禁词', '违禁词检测'] #违禁词检测
    ['图片检测', '图片鉴黄', '涩图检测', '色图检测'] #图片检测
所有功能默认开
"""
__help_plugin_name__ = "简易群管"

__permission__ = 1
__help__version__ = '0.2.0'

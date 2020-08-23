package top.parksi.bot.plugins

import net.lz1998.cq.event.message.CQDiscussMessageEvent
import net.lz1998.cq.event.message.CQGroupMessageEvent
import net.lz1998.cq.event.message.CQPrivateMessageEvent
import net.lz1998.cq.event.meta.CQHeartBeatMetaEvent
import net.lz1998.cq.event.meta.CQLifecycleMetaEvent
import net.lz1998.cq.event.notice.*
import net.lz1998.cq.event.request.CQFriendRequestEvent
import net.lz1998.cq.event.request.CQGroupRequestEvent
import net.lz1998.cq.robot.CQPlugin
import net.lz1998.cq.robot.CoolQ
import org.springframework.stereotype.Component
import top.parksi.bot.tools.Log

@Component
class BashFunc : CQPlugin() {
    override fun onHeartBeatMeta(cq: CoolQ?, event: CQHeartBeatMetaEvent?): Int {
        val time = Log().getNowTime()
        println("[Bot] [$time] [HeartBeatMeta]>> RESAVE A Heartbeat package")
        return MESSAGE_IGNORE
    }

    override fun onPrivateMessage(cq: CoolQ?, event: CQPrivateMessageEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [PrivateMessage] [${event?.sender?.userId} ${event?.sender?.nickname}]>> ${event?.message}""")
        return MESSAGE_IGNORE
    }

    override fun onGroupMessage(cq: CoolQ?, event: CQGroupMessageEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [GroupMessage] [${event?.sender?.userId} ${event?.sender?.nickname}]>> ${event?.message}""")
        return MESSAGE_IGNORE
    }

    override fun onDiscussMessage(cq: CoolQ?, event: CQDiscussMessageEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [DiscussMessage] [${event?.sender?.userId} ${event?.sender?.nickname}]>> ${event?.message}""")
        return MESSAGE_IGNORE
    }

    override fun onGroupUploadNotice(cq: CoolQ?, event: CQGroupUploadNoticeEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [GroupNotice]>> ${event?.groupId}->${event?.userId} Upload a file: ${event?.file?.name}(${event?.file?.size}Byte)""")
        return MESSAGE_IGNORE
    }

    override fun onGroupAdminNotice(cq: CoolQ?, event: CQGroupAdminNoticeEvent?): Int {
        val time = Log().getNowTime()
        if (event?.subType == "set") {
            println("""[Bot] [$time] [GroupNotice]>> ${event.groupId}->add an admin ${event.userId}""")
        } else {
            println("""[Bot] [$time] [GroupNotice]>> ${event?.groupId}->less an admin ${event?.userId}""")
        }
        return MESSAGE_IGNORE
    }

    override fun onGroupDecreaseNotice(cq: CoolQ?, event: CQGroupDecreaseNoticeEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [GroupNotice]>> ${event?.groupId}->lost one member ${event?.userId}""")
        return MESSAGE_IGNORE
    }

    override fun onGroupIncreaseNotice(cq: CoolQ?, event: CQGroupIncreaseNoticeEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [GroupNotice]>> ${event?.groupId}->add one member ${event?.userId}""")
        return MESSAGE_IGNORE
    }

    override fun onGroupBanNotice(cq: CoolQ?, event: CQGroupBanNoticeEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [GroupNotice]>> ${event?.groupId}->${event?.userId} is banned for ${event?.duration} seconds""")
        return MESSAGE_IGNORE
    }

    override fun onGroupRequest(cq: CoolQ?, event: CQGroupRequestEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [GroupRequest]>> ${event?.groupId}->${event?.userId} want join this group""")
        return MESSAGE_IGNORE
    }

    override fun onFriendAddNotice(cq: CoolQ?, event: CQFriendAddNoticeEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [FriendNotice]>> ${event?.userId} has become friends""")
        return MESSAGE_IGNORE
    }

    override fun onFriendRequest(cq: CoolQ?, event: CQFriendRequestEvent?): Int {
        val time = Log().getNowTime()
        println("""[Bot] [$time] [FriendNotice]>> ${event?.userId} wants to be friends""")
        return MESSAGE_IGNORE
    }

}
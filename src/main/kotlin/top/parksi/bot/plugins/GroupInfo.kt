package top.parksi.bot.plugins

import net.lz1998.cq.event.message.CQGroupMessageEvent
import net.lz1998.cq.robot.CQPlugin
import net.lz1998.cq.robot.CoolQ
import org.springframework.stereotype.Component
import top.parksi.bot.tools.Log


@Component
class GroupInfo : CQPlugin() {

    override fun onGroupMessage(cq: CoolQ?, event: CQGroupMessageEvent?): Int {
        if (event?.message == ".info") {
            //println("Resave Command '.info' From Group ${event.groupId}")
            Log().logLevelInfo("RESAVE COMMAND '.info' FROM ${event.groupId}")
            val groupInfo = cq?.getGroupInfo(event.groupId, false)
            val groupName = groupInfo?.data?.groupName
            val groupNowMember = groupInfo?.data?.memberCount
            val groupMaxMember = groupInfo?.data?.maxMemberCount
            cq?.sendGroupMsg(event.groupId,
                             """Name: $groupName
                                 |Id: ${event.groupId}
                                 |Number of members: $groupNowMember
                                 |Maximum number of members: $groupMaxMember
                             """.trimMargin(),
                            false)
        }
        return MESSAGE_BLOCK
    }
}
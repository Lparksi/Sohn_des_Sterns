package top.parksi.bot.tools

import java.text.SimpleDateFormat
import java.util.Date

// TODO: 2020/8/22 实现日志功能

open class Log() {
    private fun logBash(text: String?, level: String?): Unit {
        val bot = "Bot"
        val time = getNowTime()
        println("[$bot] [$time] [$level]>> $text")
    }

    fun getNowTime(): String? {
        val sdf = SimpleDateFormat()
        sdf.applyPattern("yyyy-MM-dd HH:mm:ss a")
        val data = Date()
        return sdf.format(data)
    }

    fun logLevelDebug(text: String) {
        logBash(text, "DEBUG")
    }

    fun logLevelInfo(text: String) {
        logBash(text, "INFO")
    }

    fun logLevelWrong(text: String) {
        logBash(text, "WRONG")
    }

    fun logLevelError(text: String) {
        logBash(text, "ERROR")
    }
}
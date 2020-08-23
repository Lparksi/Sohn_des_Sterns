package top.parksi.bot.plugins

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication


@SpringBootApplication
class Bot

fun main(args: Array<String>) {
    runApplication<Bot>(*args)
}

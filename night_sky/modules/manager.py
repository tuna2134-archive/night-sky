from jishaku import Feature


class Manager(Feature):
    
    @Feature.Command(parent="ns", name="close")
    async def close(self, ctx):
        m = await ctx.send("Closing...🔄")
        await self.bot.ipcs.close()
        await ctx.send("Closed ✅")
        
    @Feature.Command(parent="ns", name="reconnect")
    async def reconnect(self, ctx):
        m = await ctx.send("Reconnecting...🔄")
        await self.bot.ipcs.reconnect()
        await ctx.send("Reconnected ✅")
        
    @Feature.Command(parent="ns", name="send")
    async def send(self, ctx, type_, data):
        await self.bot.ipcs.request(eventtype=type_, data=data)
        await ctx.send("Sended ✅")

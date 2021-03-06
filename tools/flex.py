from SCons.Script import *

def addFlexBuilder(env):

	FlexAction = SCons.Action.Action("$FLEXCOM", "$FLEXCOMSTR")
	
	env["FLEX"]      = env.Detect("flex")
	env["FLEXCOM"] = "flex --header-file=${TARGET.base}.h -o $TARGET $SOURCE"
	
	def headerEmitter(target, source, env): 
		bs = SCons.Util.splitext(str(source[0].name))[0] 
		target.append(bs + '.h') 
		return (target, source) 
	
	builder = Builder(action = FlexAction,
		suffix = '.cpp',
		src_suffix = '.l',
		emitter = headerEmitter)

	env.Append(BUILDERS = {'Flex': builder})

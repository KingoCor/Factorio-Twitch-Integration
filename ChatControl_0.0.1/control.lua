script.on_init(function()
	local color = { r = 255, g = 215, b = 0, a = 1 }
	game.print( "Now chat control your game!", color )
end)

function get_random_player()
	local players = game.connected_players
	return players[ math.random(#players) ]
end

function dress_up()
	local player = get_random_player()

	local color = { r = 0, g = 255, b = 0, a = 1 }
	player.print("You've been dressed up", color)

	player.insert({ name = "power-armor-mk2", count = 1 })
	local p_armor = player.get_inventory(5)[1].grid
		p_armor.put({ name = "fusion-reactor-equipment" })
		p_armor.put({ name = "fusion-reactor-equipment" })
		p_armor.put({ name = "fusion-reactor-equipment" })
		p_armor.put({ name = "exoskeleton-equipment" })
		p_armor.put({ name = "exoskeleton-equipment" })
		p_armor.put({ name = "exoskeleton-equipment" })
		p_armor.put({ name = "exoskeleton-equipment" })
		p_armor.put({ name = "energy-shield-mk2-equipment" })
		p_armor.put({ name = "energy-shield-mk2-equipment" })
		p_armor.put({ name = "personal-roboport-mk2-equipment" })
		p_armor.put({ name = "night-vision-equipment" })
		p_armor.put({ name = "battery-mk2-equipment" })
		p_armor.put({ name = "battery-mk2-equipment" })
	player.insert({ name = "construction-robot", count = 25 })
end

function give_random_item()

	local player = get_random_player()
	local items = game.get_filtered_item_prototypes({ { filter = "stack-size", comparison = ">", value = 0 } })

	local n = 0
	local items_keys = {}

	for k, v in pairs( items ) do
		n = n + 1
		items_keys[ n ] = k
	end

	local item = items_keys[ math.random(#items_keys) ]

	player.insert({ name = item, count = math.random( 50 ) })

	local color = { r = 0, g = 255, b = 0, a = 1 }
	player.print( "You have received an item: " .. item, color )
end

function summon_biters()
	local player = get_random_player()
	local surface = player.surface
	local prototypes = game.get_filtered_entity_prototypes({ { filter = "type", type = "unit" } })

	table.remove( prototypes )

	for k, v in pairs( prototypes ) do
		local position = surface.find_non_colliding_position( k, player.position, 10, 1 )

		if position then
			surface.create_entity({ name = k, position = position, force = game.forces.enemy })
		end
	end

	local color = { r = 255, g = 0, b = 0, a = 1 }
	player.print("Good luck to survive", color)
end

function random_tp()
	local players = game.connected_players
	local player = players[ math.random( #players ) ]

	local r = 250
	local position = { math.random(player.position.x - r, player.position.x + r), math.random(player.position.y - r, player.position.y + r) }

	position = player.surface.find_non_colliding_position(player.character.name, position, 0, 1)
	player.teleport(position)

	local color = { r = 255, g = 0, b = 0, a = 1 }
	player.print("You've been teleported", color)
end

commands.add_command("dup", "dress up you", dress_up)
commands.add_command("gri", "give you random item", give_random_item)
commands.add_command("sb", "summon biters around you", summon_biters)
commands.add_command("rtp", "teleport you to random position", random_tp)

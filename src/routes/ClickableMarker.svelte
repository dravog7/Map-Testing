<script lang="ts">
	import { Icon, Marker } from 'sveaflet';
	import { createEventDispatcher } from 'svelte';
	export let position: number[];
	export let icon: string;

	const dispatch = createEventDispatcher();
	let marker: Marker;

	$: if (marker) {
		marker.on('click', (e: CustomEvent) => {
			dispatch('click', e);
		});
	}
</script>

<Marker
	latLng={[position[0], position[1]]}
	bind:instance={marker}
>
	<Icon options={{
		iconUrl: icon,
		iconSize: [24,24]
	}}></Icon>
</Marker>

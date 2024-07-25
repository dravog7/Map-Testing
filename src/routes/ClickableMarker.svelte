<script lang="ts">
	import type { LatLngTuple, LeafletMouseEvent } from 'leaflet';
	import { Icon, CircleMarker } from 'sveaflet';
	import { createEventDispatcher } from 'svelte';
	export let position: number[];
	export let color: string;

	const dispatch = createEventDispatcher();
	let marker: CircleMarker;

	$: if (marker) {
		marker.on('click', (e: CustomEvent) => {
			dispatch('click', e);
		});
	}
</script>

<CircleMarker
	latLng={[position[0], position[1]]}
	options={{ radius: 6, color: color }}
	bind:instance={marker}
></CircleMarker>

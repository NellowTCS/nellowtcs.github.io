<script lang="ts">
	import Sparkle from '#lib/components/atoms/SingleSparkle.svelte';
	import type { SparkleType } from '#lib/utils/types';
	import { onMount } from 'svelte';
	const random = (min: number, max: number) => Math.floor(Math.random() * (max - min)) + min;

	export let color: 'default' | 'primary' | 'secondary' = 'default';

	const generateSparkle = (): SparkleType => {
		return {
			id: String(random(10000, 99999)),
			createdAt: Date.now(),
			color:
				color === 'primary'
					? 'var(--color--primary)'
					: color === 'secondary'
						? 'var(--color--secondary)'
						: 'var(--color--yellow)',
			size: random(10, 20),
			style: {
				// Pick a random spot in the available space
				top: random(-10, 80) + '%',
				left: random(0, 100) + '%'
			}
		};
	};

	let sparkles: SparkleType[] = [];
	let sparklesInterval: ReturnType<typeof setInterval> | undefined;

	onMount(() => {
		const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

		const addSparkle = () => {
			const now = Date.now();
			const sparkle = generateSparkle();
			const nextSparkles = sparkles.filter((candidate) => now - candidate.createdAt < 1500);
			nextSparkles.push(sparkle);
			sparkles = nextSparkles;
		};

		const syncMotionPreference = () => {
			if (reducedMotion.matches) {
				clearInterval(sparklesInterval);
				sparklesInterval = undefined;
				sparkles = [];
			} else if (!sparklesInterval) {
				sparklesInterval = setInterval(addSparkle, 400);
			}
		};

		syncMotionPreference();
		reducedMotion.addEventListener('change', syncMotionPreference);

		return () => {
			clearInterval(sparklesInterval);
			reducedMotion.removeEventListener('change', syncMotionPreference);
		};
	});
</script>

<div class="sparkle-wrapper">
	{#each sparkles as sparkle (sparkle.id)}
		<Sparkle color={sparkle.color} size={sparkle.size} style={sparkle.style} />
	{/each}
	<span class="slot-wrapper">
		<slot />
	</span>
</div>

<style lang="scss">
	.sparkle-wrapper {
		position: relative;
		display: inline-block;

		.slot-wrapper {
			position: relative;
			z-index: 1;
		}
	}
</style>

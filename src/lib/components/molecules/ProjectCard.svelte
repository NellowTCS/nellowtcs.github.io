<script lang="ts">
	import Card from '$lib/components/atoms/Card.svelte';
	import Tag from '$lib/components/atoms/Tag.svelte';
	import Image from '../atoms/Image.svelte';

	export let title: string;
	export let coverImage: string | undefined = undefined;
	export let excerpt: string;
	export let slug: string;
	export let tags: string[] | undefined;
	export let link: string | undefined = undefined;
	export let repo: string | undefined = undefined;
</script>

<Card href="/{slug}" additionalClass="project-card {!coverImage ? 'no-image' : ''}">
	<div class="image" slot="image">
		{#if coverImage}
			<Image src={coverImage} alt="Cover image of this project" />
		{/if}
	</div>
	<div class="content" slot="content">
		<p class="title">{title}</p>
		{#if excerpt}
			<p class="text">{excerpt}</p>
		{/if}
	</div>
	<div class="footer" slot="footer">
		{#if tags?.length}
			<div class="tags">
				{#each tags.slice(0, 3) as tag}
					<Tag>{tag}</Tag>
				{/each}
			</div>
		{/if}
		<div class="links">
			{#if link}
				<a href={link} target="_blank" rel="noopener noreferrer" class="link">Live Demo</a>
			{/if}
			{#if repo}
				<a href={repo} target="_blank" rel="noopener noreferrer" class="link secondary">GitHub</a>
			{/if}
		</div>
	</div>
</Card>

<style lang="scss">
	.content {
		display: flex;
		flex-direction: column;
		gap: 0px;
		align-items: flex-start;
	}

	.title {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
		font-size: 1.2rem;
		font-family: var(--font--title);
		font-weight: 700;
	}

	.text {
		margin-top: 5px;
		font-size: 0.9rem;
		text-align: justify;
	}

	.tags {
		display: flex;
		align-items: center;
		gap: 5px;
		flex-wrap: wrap;
	}

	.footer {
		margin-top: 20px;
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.links {
		display: flex;
		gap: 8px;
	}

	.link {
		display: inline-block;
		padding: 5px 10px;
		border-radius: 20px;
		font-size: 0.75rem;
		font-weight: 700;
		text-decoration: none;
		background-color: rgb(var(--color--primary-rgb));
		color: var(--color--primary-contrast);

		&:hover {
			opacity: 0.9;
		}
	}

	.link.secondary {
		background-color: rgb(var(--color--secondary-rgb));
		color: var(--color--secondary-contrast);
	}

	:global(.project-card .image img) {
		object-fit: cover;
	}

	:global(.project-card.no-image > .image) {
		display: none;
	}
</style>

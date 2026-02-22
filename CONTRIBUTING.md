# Contributing to Ghost Labs

First off, thank you for considering contributing to Ghost Labs! It's people like you that make Ghost Labs such a great tool for collaborative development.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed**
- **Explain which behavior you expected**
- **Include screenshots if relevant**
- **Include your environment details**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the enhancement**
- **Explain why this enhancement would be useful**
- **List any alternatives you've considered**
- **Include mockups or examples if applicable**

### Pull Requests

1. Fork the repository
2. Create your feature branch from `main`
3. Make your changes
4. Add or update tests as needed
5. Ensure all tests pass
6. Update documentation
7. Commit your changes with clear messages
8. Push to your fork
9. Submit a pull request

#### Pull Request Guidelines

- Follow the existing code style
- Write clear commit messages
- Update documentation for any changed functionality
- Add tests for new features
- Ensure all tests pass
- Keep pull requests focused on a single feature/fix
- Link related issues in the PR description

## Development Setup

See the [Getting Started](README.md#getting-started) section in the README.

## Style Guidelines

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- Use conventional commit format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation
  - `style:` for formatting changes
  - `refactor:` for code refactoring
  - `test:` for tests
  - `chore:` for maintenance

### Python Style Guide

- Follow PEP 8
- Use type hints
- Write docstrings for all public functions, classes, and modules
- Maximum line length: 100 characters
- Use meaningful variable and function names

### JavaScript/TypeScript Style Guide

- Use ESLint configuration provided
- Prefer functional components with hooks
- Use TypeScript for type safety
- Use meaningful variable names
- Keep components small and focused
- Write JSDoc comments for complex functions

### Documentation Style Guide

- Use Markdown for documentation
- Keep line length reasonable (80-100 characters)
- Use proper heading hierarchy
- Include code examples where appropriate
- Keep documentation up to date with code changes

## Project Structure

Understand the project structure before contributing. See [Project Structure](README.md#project-structure) in the README.

## Testing

### Backend Tests

```bash
cd backend
pytest
pytest --cov=app tests/  # with coverage
```

### Frontend Tests

```bash
cd frontend
npm test
npm run test:coverage
```

### Integration Tests

```bash
docker-compose -f docker-compose.test.yml up
```

## Review Process

1. All pull requests require at least one review
2. Maintainers will review code for:
   - Functionality
   - Code quality
   - Tests
   - Documentation
   - Style compliance
3. Address review comments promptly
4. Once approved, maintainers will merge

## Community

- Be respectful and constructive
- Help others learn and grow
- Share knowledge and experiences
- Celebrate successes together

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Project documentation
- Release notes (for significant contributions)

## Questions?

Don't hesitate to ask questions by:
- Opening an issue
- Starting a discussion
- Reaching out to maintainers

Thank you for contributing to Ghost Labs! 🚀

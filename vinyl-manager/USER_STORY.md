# User Story: Vinyl Manager

## As a vinyl collector, I want to manage my album catalog and write reviews so that I can keep track of my collection and share my opinions.

### Acceptance Criteria

1. **Account management**
   - I can register with a username and password
   - I can log in to get a token
   - I cannot register with an existing username

2. **Album catalog**
   - I can list all albums (paginated)
   - I can filter albums by genre
   - I can view a single album's details
   - I can create an album (title, artist, genre, release year)
   - I can update an album I own
   - I cannot update an album I do not own
   - I can delete an album I own, **unless** it has reviews
   - I cannot delete an album I do not own

3. **Reviews**
   - I can view all reviews for an album
   - I can write a review (text + rating 1–5) for any album
   - I can delete my own review
   - I cannot review a non-existent album

4. **Business rules**
   - Albums with reviews cannot be deleted (409 Conflict)
   - Only the owner can modify or delete their own resources (403 Forbidden)
   - Validation errors return 422
   - Authentication is required for write operations (401 Unauthorized)
